# AWS GenAI Market Sage

A Generative AI-powered market analysis tool built on AWS services for intelligent market insights and predictions.

## Overview

AWS GenAI Market Sage leverages advanced AI models to analyze market data, generate insights, and provide predictive analytics for business decision-making.

## Project Structure

```
.
├── __pycache__/          # Python cache
├── img/                  # Image resources
├── pages/               # Application pages
├── architecture.png     # System architecture diagram
├── base.py             # Base configurations
├── company.json        # Company data configuration
├── data-01.csv         # Primary dataset
├── data-02.csv         # Secondary dataset
├── Home.py            # Main application entry point
├── libs.py            # Utility libraries
├── requirements.txt   # Project dependencies
└── README.md         # Documentation
```

## Features

- Market trend analysis
- Predictive analytics
- Company data processing
- Custom data visualization
- AWS-powered AI insights
- Multi-page interactive dashboard

## Prerequisites

- Python 3.12+
- AWS Account with appropriate permissions
- Basic understanding of market analysis
- Required Python packages (listed in requirements.txt)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/AWS-GenAI-Market-Sage.git
cd AWS-GenAI-Market-Sage
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
OPENAI_API_KEY=your_openai_key  # If using OpenAI integration
```

## Data Files

- `data-01.csv`: Primary market dataset
- `data-02.csv`: Secondary market dataset
- `company.json`: Company configuration and metadata

## Usage

1. Start the application:
```bash
python Home.py
```

2. Using the base utilities:
```python
from base import setup_environment

# Initialize environment
env = setup_environment()
```

3. Using library functions:
```python
from libs import analyze_market_data

# Analyze market data
results = analyze_market_data(dataset_path='data-01.csv')
```

## Architecture

Refer to `architecture.png` for a detailed system architecture diagram showing the interaction between different components and AWS services.

## Development

### Setting Up Development Environment

1. Install development dependencies:
```bash
pip install -r requirements-dev.txt
```

2. Configure pre-commit hooks:
```bash
pre-commit install
```

### Code Style

- Follow PEP 8 guidelines
- Use type hints
- Document functions and classes

## Testing

Run tests using pytest:
```bash
pytest tests/
```

## Security Best Practices

- Never commit sensitive credentials
- Use AWS IAM roles
- Regularly update dependencies
- Monitor AWS CloudWatch logs
- Implement data encryption

## Troubleshooting

Common issues and solutions:
- Data loading errors: Verify CSV format
- AWS connection issues: Check credentials
- Memory errors: Reduce batch size

## Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/YourFeature`)
3. Commit changes (`git commit -m 'Add YourFeature'`)
4. Push to branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.