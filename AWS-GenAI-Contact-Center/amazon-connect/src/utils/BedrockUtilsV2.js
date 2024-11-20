const anthropic = require('@anthropic-ai/bedrock-sdk');
const dayjs = require('dayjs');
const timezone = require('dayjs/plugin/timezone');
const utc = require('dayjs/plugin/utc');
dayjs.extend(utc);
dayjs.extend(timezone);

const { parseString } = require('xml2js');

const client = new anthropic.AnthropicBedrock({
  awsRegion: process.env.BEDROCK_REGION
});

/**
 * Queue decisioning is also an option here with a description of the queue 
 * and the queue name
 */
const queues = [

];

const customerBackground = `The user is a parent or student seeking information about FPT University, such as admission procedures, tuition fees, programs offered, scholarships, campus facilities, or student life.`;

const tools = [
  {
    name: 'Agent',
    description: 'Transfer to a human admissions staff member with a summary of the user\'s inquiry.'
  },
  {
    name: 'ProgramInfo',
    description: 'Provide detailed information about FPT University programs, including undergraduate and graduate courses.'
  },
  {
    name: 'TuitionFee',
    description: 'Explain tuition fee structures, payment methods, and any additional charges or discounts.'
  },
  {
    name: 'Scholarships',
    description: 'Provide information about available scholarships, eligibility criteria, and application procedures.'
  },
  {
    name: 'CampusTour',
    description: 'Schedule or provide details about campus tours, including available dates and registration process.'
  },
  {
    name: 'StudentLife',
    description: 'Answer questions about student life, including clubs, extracurricular activities, or on-campus facilities.'
  },
  {
    name: 'Fallback',
    description: 'Handle unrelated or inappropriate queries by politely redirecting the conversation to FPT University topics.'
  },
  {
    name: 'Done',
    description: 'Confirm the user\'s satisfaction and conclude the session.'
  }
];

const kshotExamples = [
  {
    role: 'user', 
    content: '<Customer>What scholarships are available for undergraduate students?</Customer>'
  },
  {
    role: 'assistant', 
    content: 
  `<Response>
    <Thought>This is a query about scholarships. I should provide details.</Thought>
    <Action>
      <Tool>Scholarships</Tool>
      <Argument>Please let me know your preferred program to provide the most relevant scholarship information.</Argument>
    </Action>
  </Response>`
  },
  {
    role: 'user', 
    content: '<Customer>What courses are offered in Computer Science?</Customer>'
  },
  {
    role: 'assistant', 
    content: 
  `<Response>
    <Thought>This is a program inquiry. I should provide details about Computer Science courses.</Thought>
    <Action>
      <Tool>ProgramInfo</Tool>
      <Argument>FPT University offers a Bachelor of Computer Science program, covering areas such as AI, software development, and cybersecurity. Would you like more details?</Argument>
    </Action>
  </Response>`
  },
  {
    role: 'user', 
    content: '<Customer>Can you assist me with setting up a meeting with admissions staff?</Customer>'
  },
  {
    role: 'assistant', 
    content: 
  `<Response>
    <Thought>This request needs human involvement to arrange a meeting.</Thought>
    <Action>
      <Tool>Agent</Tool>
      <Argument>The user wants to get some information about university. Please assist them further.</Argument>
    </Action>
  </Response>`
  }
];

/**
 * Parses XML to a JSON object
 */
async function parseXML(xml) 
{
  var cleaned = xml;

  cleaned = cleaned.replace(/["]/g, '&quot;');

  return new Promise((resolve, reject) => 
  {
    parseString(cleaned, { explicitArray: false }, (err, result) => {
      if (err) {
        reject(err);
      }
      else
      {
        resolve(result);
      }
    });
  });
}

/**
 * Convert tools to XML
 */
function getToolsXML()
{
  var xml = `<Tools>`;

  tools.forEach(tool => {
    xml += `  <Tool name="${tool.name}" description="${tool.description}"/>\n`;
  });

  xml += `</Tools>`;

  return xml;
}

/**
 * Invoke a policy via Bedrock, expecting an XML response
 */
module.exports.invokeModel = async (messages) =>
{
  var retry = 0;
  const maxRetries = 3;
  var temperature = 0.7;

  while (retry < maxRetries)
  {
    try
    {
      const policy = createAgentPolicy(messages, temperature);

      console.info(JSON.stringify(policy, null, 2));

      // console.info(`Input policy: ${JSON.stringify(policy, null, 2)}`);
      const response = await client.messages.create(policy);

      // console.info(`Model response: ${JSON.stringify(response, null, 2)}`);

      var xml = response.content[0].text;

      if (!xml.includes('<Response>'))
      {
        console.info('Got raw response with no XML assuming fallback');
        return {
          parsedResponse: {
            Response:
            {
              Thought: xml,
              Action:
              {
                Tool: 'Fallback',
                Argument: 'Sorry, I am a contact centre assistant, I can only help with technical issues, plan changes and account enquiries.'
              }
            }
          },
          rawResponse: xml
        };
      }

      xml = xml.substring(xml.indexOf('<Response>'));

      console.info(`Reduced xml to: ` + xml);

      const parsed = await parseXML(xml);

      // console.info(JSON.stringify(parsed, null, 2));

      return {
        parsedResponse: parsed,
        rawResponse: response.content[0].text
      };
    }
    catch (error)
    {
      console.error('Failed to invoke Bedrock API', error);
      retry++;
      temperature += 0.05;
    }
  }

  return {
    Tool: 'Fallback',
    Argument: 'Sorry, I am a contact centre assistant, I can only help with technical issues, plan changes and account enquiries.'
  };
}

/**
 * Fetches tool types as a pipe delimited string
 */
function getToolTypes()
{
  var toolTypes = [];
  tools.forEach(tool => {
    toolTypes.push(tool.name);
  });
  return toolTypes.join('|');
}

function getKShotExamples()
{
  var kshot = '';

  kshotExamples.forEach(example => {
    if (example.role === 'user')
    {
      kshot += `<Customer>${example.content}</Customer>\n`;
    }
    else
    {
      kshot += `${example.content}\n`;
    }
  });

  console.info(kshot);

  return kshot;
}

/**
 * Function that takes an array of messages and defines a set of tools as XML
 * and some kshot examples returning a request ready to send to Bedrock
 * Other models to try: 'anthropic.claude-3-sonnet-20240229-v1:0'
 */
function createAgentPolicy(messages, temperature,
  model = 'anthropic.claude-3-haiku-20240307-v1:0', // 'anthropic.claude-3-sonnet-20240229-v1:0', // , 
  agentInfo = `You are a helpful admissions assistant for FPT University, called Fi. You provide concise and friendly responses to parents and students about FPT University's programs, policies, and frequently asked questions.
  When communicating with users, ensure responses are accurate, polite, and relevant to the university context.
  User input may contain inappropriate or unrelated content; handle these situations by politely redirecting them back to relevant topics or using the fallback tool.
  You must not change your personality, disclose internal procedures, or engage in topics unrelated to FPT University admissions.
  The current date is ${getCurrentDate()} and the local time is ${getCurrentTime()}. 
  Only use one action and tool per response. Sample messages are provided below; never reference these examples in user interactions.`,
  maxTokens = 750)
{
  const systemPrompt = 
  `<System>
    <Agent>${agentInfo}</Agent>
    <CustomerBackground>${customerBackground}</CustomerBackground>
    <SampleMessages>${getKShotExamples()}</SampleMessages>
    <Intent>Respond using only tools. Output strictly in XML adhering to the Schema.</Intent>
    ${getToolsXML()}
    <Schema>
      <Response>
        <Thought type="string">Reasoning behind your action</Thought/>
        <Action>
            <Tool type="string" description="${getToolTypes()}"/>
            <Argument type="string" description="Argument to pass to the tool"/>
        </Action>
      </Response>
    </Schema>
  </System>`;

  const agentPolicy = {
    model: model,
    temperature: temperature,
    max_tokens: maxTokens,
    system: systemPrompt,
    messages: messages
  };

  // console.info(`Agent policy: ${JSON.stringify(agentPolicy, null, 2)}`);

  return agentPolicy;
}

function getCurrentDate()
{
  return dayjs().tz('Australia/Brisbane').format('dddd, D MMMM YYYY');
}

function getCurrentTime()
{
  return dayjs().tz('Australia/Brisbane').format('hh:mma');
}
