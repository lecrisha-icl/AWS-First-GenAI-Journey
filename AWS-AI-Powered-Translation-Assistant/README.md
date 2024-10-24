# AWS AI-Powered Translation Assistant

A proof-of-concept translation application leveraging Amazon Bedrock and Generative AI to provide real-time translation capabilities through multiple interfaces.

## Features

- **Text Translation**: Translate text with accuracy and fluency feedback
- **Chat Translation**: Real-time translation for conversational interactions
- **File Translation**: Upload and translate entire text files
- **Multiple Language Support**: Translate between various language pairs
- **Powered by Amazon Bedrock**: Utilizes state-of-the-art AI models for accurate translations

## Prerequisites

- Python 3.10
- AWS CLI installed and configured
- Access to Amazon Bedrock
- Active AWS account with appropriate permissions

## Quick Start

1. **Clone the Repository**
   ```bash
   git clone https://github.com/aws-samples/AWS-First-GenAI-Journey.git
   cd AWS-First-GenAI-Journey
   ```

2. **Set Up Virtual Environment**
   ```bash
   pip install virtualenv
   python3.10 -m venv venv

   # Activate virtual environment
   # For Linux/MacOS:
   source venv/bin/activate
   # For Windows:
   venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure AWS Credentials**
   Create a `.env` file in the root directory:
   ```bash
   profile_name=<AWS_CLI_PROFILE_NAME>
   ```

5. **Launch the Application**
   ```bash
   streamlit run Text.py
   ```

## Application Structure

- `Text.py`: Text translation interface
- `Chat.py`: Chat translation interface
- `File.py`: File upload and translation interface
- `amazon_bedrock_translation.py`: Core translation logic using Amazon Bedrock
- `requirements.txt`: Project dependencies

## Configuration

### AWS Region

The default AWS region is set to `us-east-1`. To modify the region, update the Bedrock client configuration in `prompt_finder_and_invoke_llm.py`:

```python
bedrock = boto3.client(
    'bedrock-runtime',
    'us-east-1',
    endpoint_url='https://bedrock-runtime.us-east-1.amazonaws.com'
)
```

### AI Model Selection

The application uses Claude 3 by default. To use a different model, modify the `modelId` in `amazon_bedrock_translation.py`:

```python
modelId = 'anthropic.claude-v2'  # Change to any Bedrock-supported model
```

## Usage

### Text Translation
1. Access the text translation interface
2. Enter your text in the input field
3. Select source and target languages
4. View translation with accuracy metrics

### Chat Translation
1. Open the chat interface
2. Select your target language
3. Start conversing to receive real-time translations

### File Translation
1. Navigate to the file upload interface
2. Upload your text file
3. Select the target language
4. Download the translated file

## Contributing

We welcome contributions to improve the translation assistant. Please follow standard GitHub pull request procedures to submit your changes.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For issues and questions:
- Create a GitHub issue
- Contact AWS Support for Bedrock-related questions
- Check AWS documentation for service-specific details

## Additional Resources

- [Amazon Bedrock Documentation](https://docs.aws.amazon.com/bedrock/)
- [AWS CLI Configuration Guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html)
- [Python Virtual Environment Guide](https://docs.python.org/3/library/venv.html)