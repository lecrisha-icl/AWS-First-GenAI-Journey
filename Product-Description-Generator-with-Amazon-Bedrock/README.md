# Product Description Generator with Amazon Bedrock

An AI-powered product description generator that creates compelling, SEO-friendly product descriptions using Amazon Bedrock's language models.

## Project Structure

```
.
├── check_in/                  # Check-in module
├── check_uniform/             # Uniformity checker
├── content_moderation/        # Content moderation
├── content_moderation.1/      # Enhanced moderation
├── product_description/       # Core description generator
├── Home.py                   # Main application
├── image_lib.py              # Image processing
├── Libs.py                   # Utility functions
├── Main.py                   # Application logic
└── requirements.txt          # Dependencies
```

## Features

- AI-powered description generation
- SEO optimization
- Multi-language support
- Image integration
- Content moderation
- Style customization
- Bulk processing
- Brand voice consistency
- Keyword optimization
- Category-specific templates

## Prerequisites

- Python 3.12+
- AWS Account with Bedrock access
- Required Python packages (see requirements.txt)
- Basic product knowledge

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/Product-Description-Generator.git
cd Product-Description-Generator
```

2. Create virtual environment:
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
MODEL_TEMPERATURE=0.7
MAX_TOKENS=2000
```

## Usage

### Basic Description Generation

```python
from product_description import generate_description

description = generate_description(
    product_name="Ergonomic Office Chair",
    features=["360-degree swivel", "lumbar support", "adjustable height"],
    style="professional",
    tone="persuasive"
)
```

### Bulk Processing

```python
from Main import batch_generate_descriptions

descriptions = batch_generate_descriptions(
    products_file="products.csv",
    output_format="json"
)
```

### Content Moderation

```python
from content_moderation import moderate_description

moderated_content = moderate_description(
    description="Product description text",
    brand_guidelines=brand_rules,
    check_compliance=True
)
```

## Description Templates

### Basic Template
```python
template = {
    "headline": "{product_name} - {key_benefit}",
    "opening": "Discover the {adjective} {product_name}...",
    "features": ["Feature 1: {detail}", "Feature 2: {detail}"],
    "benefits": ["Benefit 1: {explanation}", "Benefit 2: {explanation}"],
    "call_to_action": "Get your {product_name} today!"
}
```

## Customization Options

### Tone Settings
- Professional
- Casual
- Luxury
- Technical
- Friendly
- Persuasive

### Style Parameters
- Length (short, medium, long)
- Format (paragraph, bullet points)
- SEO density
- Keyword placement
- Brand voice alignment

## Best Practices

1. Product Information
   - Provide accurate specifications
   - Include key features
   - Specify target audience
   - Define unique selling points

2. SEO Optimization
   - Key phrase research
   - Natural keyword integration
   - Meta description generation
   - Search intent alignment

3. Content Quality
   - Grammar checking
   - Plagiarism detection
   - Brand voice consistency
   - Value proposition clarity

## Performance Optimization

- Batch processing
- Template caching
- Response optimization
- Resource management
- Request queuing

## Error Handling

Common issues and solutions:
- Missing product data
- API rate limits
- Template mismatches
- Content moderation flags

## Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/YourFeature`)
3. Commit changes (`git commit -m 'Add YourFeature'`)
4. Push to branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.