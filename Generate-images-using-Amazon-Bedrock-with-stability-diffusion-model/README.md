# Generate Images Using Amazon Bedrock with Stability Diffusion Model

A Python application that leverages Amazon Bedrock and the Stability Diffusion model to generate high-quality images from text prompts.

## Project Structure

```
.
├── images/              # Generated images directory
├── prompt/             # Prompt templates and examples
├── app.py             # Main application
└── requirements.txt   # Project dependencies
```

## Features

- Text-to-image generation
- Prompt optimization
- Customizable image parameters
- Batch image generation
- Multiple style support
- Image variation generation
- Resolution control
- Style mixing capabilities

## Prerequisites

- Python 3.12+
- AWS Account with Bedrock access
- Appropriate IAM permissions
- Required Python packages (see requirements.txt)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/Generate-Images-Amazon-Bedrock-Stability.git
cd Generate-Images-Amazon-Bedrock-Stability
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

## Environment Setup

Create a `.env` file in the root directory:
```
AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key
AWS_DEFAULT_REGION=your_region
IMAGE_OUTPUT_DIR=./images
```

## Usage

### Basic Image Generation

```python
from app import generate_image

image = generate_image(
    prompt="A serene lake at sunset with mountains in the background",
    style="realistic",
    size=(1024, 1024)
)
```

### Batch Generation

```python
from app import batch_generate

images = batch_generate(
    prompts=["prompt1", "prompt2", "prompt3"],
    base_style="photographic"
)
```

## Prompt Guidelines

### Effective Prompt Structure
```
[Style] [Subject] [Details] [Lighting] [Composition]

Example:
"Cinematic photograph of a majestic eagle soaring through a stormy sky, dramatic lighting, ultra-detailed feathers, 4K resolution"
```

### Style Keywords
- Photorealistic
- Cinematic
- Digital Art
- Oil Painting
- Watercolor
- Studio Photography
- Abstract

## Configuration Options

### Image Parameters
```python
parameters = {
    "width": 1024,
    "height": 1024,
    "steps": 50,
    "cfg_scale": 7.5,
    "style_preset": "photographic",
    "seed": 42  # Optional for reproducibility
}
```

### Style Mixing
```python
style_config = {
    "style1_weight": 0.7,
    "style2_weight": 0.3,
    "style1": "photographic",
    "style2": "digital-art"
}
```

## Best Practices

1. Prompt Engineering
   - Be specific and detailed
   - Use descriptive adjectives
   - Include style preferences
   - Specify composition details

2. Image Quality
   - Use appropriate resolution
   - Adjust step count for quality
   - Fine-tune CFG scale
   - Consider style presets

3. Performance
   - Batch similar requests
   - Cache common generations
   - Monitor API usage
   - Optimize prompt length

## Error Handling

Common issues and solutions:
- API rate limits
- Resource constraints
- Invalid prompt format
- Image generation failures

## Security

- Secure credential management
- Content filtering
- Access control
- Usage monitoring
- Regular audits

## Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/YourFeature`)
3. Commit changes (`git commit -m 'Add YourFeature'`)
4. Push to branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.