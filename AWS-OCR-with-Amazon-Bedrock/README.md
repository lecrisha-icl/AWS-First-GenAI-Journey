# AWS OCR with Amazon Bedrock

A Python-based OCR (Optical Character Recognition) solution leveraging Amazon Bedrock and Claude 3 models for accurate text extraction from images.

## Overview

This project provides OCR capabilities using two main approaches:
1. Direct OCR using Claude 3 with Boto3
2. Enhanced OCR using Claude 3 with LangChain integration

## Project Structure

```
.
├── app.py                    # Main application entry point
├── claude3_boto3_ocr.py      # Claude 3 OCR implementation using Boto3
├── claude3_langchain_ocr.py  # Claude 3 OCR implementation using LangChain
└── requirements.txt          # Project dependencies
```

## Prerequisites

- Python 3.12+
- AWS Account with Bedrock access
- Appropriate IAM permissions for Bedrock
- Claude 3 model access

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/AWS-OCR-with-Amazon-Bedrock.git
cd AWS-OCR-with-Amazon-Bedrock
```

2. Create and activate virtual environment:
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On Unix or MacOS
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Environment Configuration

Create a `.env` file in the root directory:
```
AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key
AWS_DEFAULT_REGION=your_region
```

## Usage

### Using Boto3 Implementation

```python
from claude3_boto3_ocr import extract_text

# Extract text from an image
text = extract_text('path/to/your/image.jpg')
```

### Using LangChain Implementation

```python
from claude3_langchain_ocr import process_document

# Process document with enhanced features
result = process_document('path/to/your/document.pdf')
```

### Running the Application

```bash
python app.py --input path/to/image --output path/to/result
```

## Features

- High-accuracy text extraction
- Support for multiple image formats
- PDF document support
- Table structure recognition
- Multi-language support
- Custom output formatting

## Best Practices

1. Image Preparation:
   - Ensure good image quality
   - Proper lighting and contrast
   - Minimum resolution of 300 DPI
   - Supported formats: JPG, PNG, PDF

2. Error Handling:
   - Implement proper error handling for API calls
   - Validate input files before processing
   - Check output quality metrics

## Performance Optimization

- Use appropriate image preprocessing
- Batch processing for multiple images
- Implement caching when possible
- Monitor API usage and costs

## Security

- Keep AWS credentials secure
- Use IAM roles with minimum required permissions
- Implement input validation
- Monitor usage patterns

## Troubleshooting

Common issues and solutions:
- Image format not supported: Convert to supported format
- Text not recognized: Check image quality
- API timeout: Adjust request timeout settings
- Authentication errors: Verify AWS credentials

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.