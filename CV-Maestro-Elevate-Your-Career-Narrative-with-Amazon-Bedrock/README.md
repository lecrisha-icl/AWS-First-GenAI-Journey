# CV Maestro: Elevate Your Career Narrative

An AI-powered CV enhancement tool built with Amazon Bedrock to help professionals create compelling career narratives and stand out in their job applications.

## Project Structure

```
.
├── __pycache__/         # Python cache directory
├── pages/              # Application pages
├── Architecture.png    # System architecture diagram
├── get-pip.py         # Pip installer
├── Home.py            # Main application entry
├── recruitment_lib.py  # Recruitment utilities
└── requirements.txt   # Project dependencies
```

## Features

- AI-powered CV content enhancement
- Professional achievement highlighting
- Skills gap analysis
- Industry-specific keyword optimization
- Action verb suggestions
- Accomplishment quantification
- Personal brand development
- ATS (Applicant Tracking System) optimization

## Prerequisites

- Python 3.12+
- AWS Account with Bedrock access
- Basic understanding of CV/resume writing
- Required Python packages (listed in requirements.txt)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/CV-Maestro.git
cd CV-Maestro
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
python get-pip.py
pip install -r requirements.txt
```

## Environment Configuration

Create a `.env` file in the root directory:
```
AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key
AWS_DEFAULT_REGION=your_region
MODEL_TEMPERATURE=0.7
```

## Usage

### Starting the Application

```bash
python Home.py
```

### Using Recruitment Library

```python
from recruitment_lib import enhance_experience

# Enhance job experience
enhanced_content = enhance_experience(
    original_text="Managed a team of developers",
    industry="Technology",
    level="Senior"
)
```

## Features in Detail

### 1. Content Enhancement
- Professional tone adjustment
- Impact statement generation
- Achievement quantification
- Skills highlighting

### 2. ATS Optimization
- Keyword analysis
- Format compatibility
- Industry-specific terms
- Ranking improvement

### 3. Personal Branding
- Unique value proposition
- Professional narrative
- Core competencies
- Career progression

## Best Practices

### CV Writing Guidelines
- Use strong action verbs
- Quantify achievements
- Focus on results
- Maintain consistency
- Tailor for specific roles

### AI Enhancement Tips
- Provide detailed input
- Review AI suggestions
- Maintain authenticity
- Cross-reference skills
- Verify industry terms

## Architecture

The `Architecture.png` diagram shows:
- System components
- Data flow
- AWS service integration
- Processing pipeline

## Performance Tips

- Pre-process content
- Use industry templates
- Batch process updates
- Cache common enhancements
- Optimize API calls

## Security

- Secure data handling
- Content encryption
- Access control
- Privacy protection
- Regular audits

## Troubleshooting

Common issues and solutions:
- Content processing errors
- API rate limits
- Format compatibility
- Enhancement quality

## Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/YourFeature`)
3. Commit changes (`git commit -m 'Add YourFeature'`)
4. Push to branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.