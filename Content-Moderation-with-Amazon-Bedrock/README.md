# Content Moderation with Amazon Bedrock

An intelligent content moderation system powered by Amazon Bedrock for automated content filtering and analysis.

## Project Structure

```
.
├── check_in/               # Check-in verification module
├── check_uniform/          # Uniform content checking
├── content_moderation/     # Core moderation module
├── content_moderation.1/   # Extended moderation features
├── product_description/    # Product content analysis
├── Home.py                # Main application entry
├── image_lib.py           # Image processing utilities
├── Libs.py               # Common utility functions
├── Main.py               # Application core
└── requirements.txt      # Project dependencies
```

## Features

- Real-time content moderation
- Multi-modal content analysis (text, images)
- Customizable moderation rules
- Content classification
- Automated content filtering
- Detailed moderation reports
- Batch processing capabilities

## Prerequisites

- Python 3.12+
- AWS Account with Bedrock access
- Required permissions for AWS services
- Basic understanding of content moderation principles

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/Content-Moderation-with-Amazon-Bedrock.git
cd Content-Moderation-with-Amazon-Bedrock
```

2. Set up virtual environment:
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
MODERATION_THRESHOLD=0.8
```

## Usage

### Basic Content Moderation

```python
from content_moderation import moderate_content

result = moderate_content(
    content="Your content here",
    content_type="text"
)
```

### Image Moderation

```python
from image_lib import process_image
from content_moderation import moderate_image

# Process and moderate image
image = process_image("path/to/image.jpg")
result = moderate_image(image)
```

### Batch Processing

```python
from Main import batch_moderate

results = batch_moderate(
    content_list=["content1", "content2"],
    content_type="text"
)
```

## Moderation Rules

Customize moderation rules in `content_moderation/rules.json`:
```json
{
    "profanity_threshold": 0.8,
    "sensitive_content_threshold": 0.7,
    "violence_threshold": 0.9
}
```

## Content Categories

The system moderates content across multiple categories:
- Profanity
- Adult content
- Violence
- Hate speech
- Personal information
- Spam/Scam content
- Custom categories

## Performance Optimization

- Batch processing for multiple items
- Caching for frequent content
- Optimized image processing
- Rate limiting implementation

## API Reference

### Moderation API

```python
moderate_content(
    content: str,
    content_type: str,
    threshold: float = 0.8
) -> ModerationResult
```

### Image Processing API

```python
process_image(
    image_path: str,
    resize: bool = True,
    max_size: tuple = (1024, 1024)
) -> ProcessedImage
```

## Security Best Practices

- Input validation
- Content encryption
- Secure API endpoints
- Access control implementation
- Regular security audits

## Monitoring and Logging

- CloudWatch integration
- Performance metrics
- Error tracking
- Moderation statistics
- Usage analytics

## Troubleshooting

Common issues and solutions:
- API rate limits
- Image format support
- Content size limits
- Processing timeouts

## Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/YourFeature`)
3. Commit changes (`git commit -m 'Add YourFeature'`)
4. Push to branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.