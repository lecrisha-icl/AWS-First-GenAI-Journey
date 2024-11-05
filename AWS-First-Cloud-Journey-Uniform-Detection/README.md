# AWS First Cloud Journey Uniform Detection

An AI-powered system for uniform detection and compliance checking using AWS cloud services. This project helps organizations automate the process of checking uniform compliance through image processing and machine learning.

## Features

- Uniform compliance checking
- Content moderation
- Product description analysis
- Image processing capabilities
- Real-time check-in verification

## System Components

- `check_in/`: Check-in verification module
- `check_uniform/`: Uniform detection and analysis
- `content_moderation/`: Content filtering and moderation
- `product_description/`: Product analysis tools
- `image_lib.py`: Image processing utilities
- `Libs.py`: Common utility functions
- `Main.py`: Application entry point
- `Home.py`: Home page interface

## Prerequisites

- Python 3.12+
- AWS Account with required services:
  - Amazon Rekognition
  - Amazon S3
  - AWS Lambda
  - Amazon SageMaker (if using custom models)
- Required Python packages (see requirements.txt)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/AWS-First-Cloud-Journey-Uniform-Detection.git
cd AWS-First-Cloud-Journey-Uniform-Detection
```

2. Set up Python virtual environment:
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
S3_BUCKET_NAME=your_bucket_name
REKOGNITION_MODEL_ARN=your_model_arn
```

## Usage

1. Start the application:
```bash
python Main.py
```

2. Using the check-in module:
```python
from check_in import verify_check_in

result = verify_check_in(image_path)
```

3. Uniform compliance checking:
```python
from check_uniform import check_uniform_compliance

compliance_result = check_uniform_compliance(image_path)
```

## Image Processing

The `image_lib.py` module provides utilities for:
- Image preprocessing
- Format conversion
- Size optimization
- Quality enhancement

Example:
```python
from image_lib import process_image

processed_image = process_image(
    image_path,
    target_size=(800, 600),
    enhance_quality=True
)
```

## Content Moderation

Content moderation features include:
- Inappropriate content detection
- Uniform compliance verification
- Brand guideline checking

## Development

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Testing

Run tests using:
```bash
python -m pytest tests/
```

## Troubleshooting

Common issues:
- AWS credentials not configured correctly
- Image format not supported
- Model inference timeout

## Security

- Keep AWS credentials secure
- Use IAM roles with minimum required permissions
- Regularly update dependencies
- Monitor AWS CloudWatch logs

## License

This project is licensed under the MIT License - see the LICENSE file for details.