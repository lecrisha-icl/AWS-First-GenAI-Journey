# AWS First GenAI - Image Analysis Using Amazon Bedrock

A proof-of-concept application demonstrating image analysis capabilities using Amazon Bedrock and Anthropic's Multi-Modal Generative AI models. The application provides a streamlit-based interface where users can upload images (JPEG, PNG, or PDF) and receive AI-generated descriptions.

## Architecture Overview

The application follows a simple flow:
1. User uploads an image through the Streamlit frontend (app.py)
2. The application invokes Amazon Bedrock to analyze the image (analyze_images.py)
3. Generated description is displayed back to the user in the Streamlit interface

## Prerequisites

- Amazon Bedrock access with appropriate model permissions configured in the console
- AWS CLI credentials configured
- Python 3.10 (recommended for package stability)
- Basic familiarity with Python virtual environments

## Installation

1. Clone the repository:
```bash
git clone [repository-url]
cd aws-first-genai
```

2. Create and activate a Python virtual environment:
```bash
pip install virtualenv
python3.10 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure environment variables:
   - Create a `.env` file in the project root
   - Add your AWS CLI profile configuration:
   ```
   profile_name=<AWS_CLI_PROFILE_NAME>
   ```

## Configuration

### Model Settings
The application uses Amazon Bedrock with Anthropic's Claude 3 model. You can customize the model parameters in `analyze_images.py`:

```python
brclient = boto3.client('bedrock-runtime', 'us-east-1', 
    endpoint_url='https://bedrock-runtime.us-east-1.amazonaws.com',
    config=config)

model_id = "anthropic.claude-3-sonnet-20240229-v1:0"
```

### Prompt Customization
You can modify the system prompt in `analyze_images.py` to tailor the image analysis for specific use cases:

```python
system_prompt = """You are an expert in image analysis and classification. 
The question will be contained within the <question></question> tags..."""
```

## Usage

1. Start the application:
```bash
streamlit run app.py
```

2. Open your web browser to the provided URL (typically http://localhost:8501)

3. Upload an image (supported formats: JPEG, PNG, PDF)

4. View the AI-generated description and analysis

## Project Structure

- `app.py`: Streamlit frontend application
- `analyze_images.py`: Core logic for image analysis using Amazon Bedrock
- `requirements.txt`: Project dependencies

## Important Notes

- Ensure your AWS CLI profile has the necessary permissions for Amazon Bedrock
- Only certain models in Amazon Bedrock support image analysis
- Single-page images are currently supported

## Customization Options

1. **Region and Endpoint**: Modify the AWS region and endpoint URL in `analyze_images.py` based on your requirements

2. **Use Case Specific Prompts**: Customize the system prompt for industry-specific image analysis needs

3. **Response Format**: Adjust the response structure by modifying the prompt template and parsing logic

## Troubleshooting

1. If you encounter AWS credential issues:
   - Verify your AWS CLI profile configuration
   - Ensure your profile has appropriate Bedrock permissions

2. For Python environment issues:
   - Confirm Python 3.10 is correctly installed
   - Verify all dependencies are installed in your virtual environment

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

