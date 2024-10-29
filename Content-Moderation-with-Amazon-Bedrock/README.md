# AWS First GenAI

## Overview 
This is a simple demo of Amazon Bedrock and Anthropic Claude 3.5 model with langchain library. For more detail please reference the following links:
- [Amazon Bedrock](https://aws.amazon.com/bedrock/)
- [Anthropic Claude 3.5](https://www.anthropic.com/claude)

## Prerequisites
- [Python Installation Guide](https://docs.python-guide.org/starting/install3/linux/)
- [AWS CLI Setup Guide](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-quickstart.html)
- Python 3.10 or higher
- AWS account with Bedrock access

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone 
   ```

2. Navigate to project directory:
   ```bash
   cd AWS-First-GenAI
   ```

3. Create and activate Python virtual environment:
   ```bash
   # Windows
   python -m venv venv-python3.10
   .\venv-python3.10\Scripts\activate

   # macOS/Linux
   python3.10 -m venv venv-python3.10
   source venv-python3.10/bin/activate
   ```

4. Install required packages:
   ```bash
   pip3 install -r requirements.txt
   ```

5. Run the Streamlit application:
   ```bash
   streamlit run Home.py --server.port 8080
   ```

## Important Resources
- [Introduction to Prompt Design](https://docs.anthropic.com/claude/docs/introduction-to-prompt-design)

## Features
- Integration with Amazon Bedrock
- Anthropic Claude 3.5 implementation
- Streamlit web interface
- LangChain implementation

## Configuration
Ensure your AWS credentials are properly configured with access to Bedrock service. You can configure AWS credentials using:
```bash
aws configure
```

To use Claude 3.5 in Bedrock, make sure to specify the model ID as "anthropic.claude-3.5-sonnet" in your configuration.

## Dependencies
- langchain==0.0.343
- streamlit
- boto3
- botocore
- python-dotenv
- Additional dependencies listed in requirements.txt

## Support
For more information about the components used:
- Amazon Bedrock: [AWS Bedrock Documentation](https://aws.amazon.com/bedrock/)
- Anthropic Claude: [Claude Documentation](https://www.anthropic.com/claude)
- LangChain: [LangChain Documentation](https://python.langchain.com/docs/get_started/introduction.html)