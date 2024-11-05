# AWS AI-Powered Translation Assistant

A Python-based translation assistant powered by Amazon Bedrock AI services for accurate and efficient language translation.

## Features

- Multiple language support
- AWS Bedrock integration for AI-powered translation
- Simple Python interface
- Support for text files and direct input

## Prerequisites

- Python 3.12+
- AWS Account with Bedrock access
- AWS credentials configured

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/AWS-AI-Powered-Translation-Assistant.git
cd AWS-AI-Powered-Translation-Assistant
```

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
AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key
AWS_DEFAULT_REGION=your_region
```

## Usage

Run the translation script:
```bash
python Text.py
```

The `amazon_bedrock_translation.py` script provides the core translation functionality:
```python
from amazon_bedrock_translation import translate_text

# Example usage
translated_text = translate_text(
    source_text="Hello, world!",
    source_language="en",
    target_language="es"
)
```

## Project Structure

```
.
├── images/                  # Image resources
├── pages/                   # Additional page modules
├── amazon_bedrock_translation.py  # Core translation logic
├── Text.py                 # Main application script
├── requirements.txt        # Project dependencies
└── README.md              # Project documentation
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Security

- Never commit your AWS credentials to version control
- Keep your .env file secure and local
- Follow AWS security best practices

## Support

For support, please open an issue in the repository or contact the project maintainers.