# AWS GenAI Code Security Review

An interactive UI website build by Streamlit, backed by Amazon Bedrock to review security issue in your code

## Features

- Scan single code file
- Scan entier Github repository
- Using Amazon Bedrock - Model Claude 3 to analyze source code

## Prerequisites

- Python 3.12+
- AWS Account with appropriate permissions
- Basic understanding of Python AWS services, and Generative AI

## Installation

1. Clone the repository

2. Create and activate a virtual environment:
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On Unix or MacOS
source venv/bin/activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

## Environment Setup

Create a `.env` file in the root directory:
```
MAX_TOKENS = 2000

ASSISTANT_ROLE = "As a security expert, you will evaluate the provided code to identify vulnerabilities and risks. Look for common attack vectors such as SQL injection, XSS, buffer overflow, and remote code execution. Examine the code for secure coding practices like input validation, output sanitization, authentication, access controls, and error handling. Based on your findings, provide recommendations for improving the code's security posture and mitigating identified risks. Your report should include:

1. A detailed description of each vulnerability found.
2. Its severity.
3. A snippet of the affected code.
4. A mitigation walkthrough in plain English.
5. The mitigated code follow security best practice.

Ensure the following output format:
- ### Vulnerability Type: <output>
- Description: <output>
- ###### Severity: <output>
- ###### A snippet of affected code:
```
<output>
```
- ###### Mitigation walkthrough:
<output>
- ###### Improved code:
```
<output>
```
---

Focus on clarity and detail to ensure that your analysis is thorough and understandable."

MODEL_ID = 'anthropic.claude-3-haiku-20240307-v1:0'
QUOTAS_FILE_ANALLYZING = 2
AWS_REGION = 'us-west-2'
```
You can change the prompt statement, Bedrock model if you want (but it might be different in payload between different model)

## Project Structure

```
.
├── code_review/               
├──     bedrock_analyze.py          # Handle logic to interact with Bedrock model
├──     git_handler.py              # Handle logic analyze Github repo scanning security issues
├── report/           
├──     2024-11-13_13-46-53.md      # Report about security problem in markdown format
├── source/                     
├──     <cloned_git_repo>/          # The directory that we will clone to local to analyze, it is generated automatically        
├── .env                            # Environment variables
├── app.py                          # Main logic handle application
├── requirements.txt                # Packages information
└── README.md                       # Document    
```

## Running the Application

Start the application:
```bash
streamlit run app.py
```

## Development

To contribute to the project:

1. Fork the repository
2. Create a new branch (`git checkout -b feature-name`)
3. Make your changes
4. Submit a pull request

## Troubleshooting

Common issues and solutions:
- AWS credentials not working: Verify `.env` file configuration
- Import errors: Check virtual environment activation
- Page loading issues: Verify all dependencies are installed

## Support

For support:
- Open an issue in the repository
- Check existing documentation
- Contact the development team

## License

This project is licensed under the MIT License - see the LICENSE file for details.