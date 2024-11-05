# HR Luminary with Amazon Bedrock

An intelligent HR automation platform powered by Amazon Bedrock, designed to streamline recruitment processes and enhance HR operations.

## Project Structure

```
.
├── __pycache__/         # Python cache directory
├── pages/              # Application pages
├── Architecture.png    # System architecture diagram
├── get-pip.py         # Pip installer
├── Home.py            # Main application file
├── recruitment_lib.py  # Recruitment utilities
└── requirements.txt   # Project dependencies
```

## Features

- Resume parsing and analysis
- Candidate skill matching
- Automated screening
- Interview scheduling
- Performance analytics
- Job description optimization
- Candidate communication
- HR document processing
- Recruitment workflow automation
- Diversity and inclusion tools

## Prerequisites

- Python 3.12+
- AWS Account with Bedrock access
- Required Python packages (listed in requirements.txt)
- Basic understanding of HR processes

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/HR-Luminary.git
cd HR-Luminary
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
AI_MODEL_TEMPERATURE=0.7
DATABASE_URL=your_database_url
```

## Usage Examples

### Resume Analysis

```python
from recruitment_lib import analyze_resume

analysis = analyze_resume(
    resume_path="path/to/resume.pdf",
    job_requirements=["Python", "AWS", "Machine Learning"]
)
```

### Job Description Optimization

```python
from recruitment_lib import optimize_job_description

optimized_jd = optimize_job_description(
    job_description="Original JD text",
    include_keywords=True,
    enhance_inclusivity=True
)
```

## Key Features

### 1. Candidate Management
- Resume parsing
- Skill matching
- Experience validation
- Education verification
- Portfolio analysis

### 2. Recruitment Automation
- Application screening
- Interview scheduling
- Email communication
- Status tracking
- Feedback collection

### 3. Analytics & Reporting
- Recruitment metrics
- Pipeline analytics
- Time-to-hire tracking
- Cost analysis
- Diversity metrics

### 4. Document Processing
- Contract generation
- Offer letter creation
- Policy documents
- Onboarding materials
- Compliance checking

## Best Practices

### Recruitment Process
- Standardized evaluation
- Bias mitigation
- Regular calibration
- Documentation
- Compliance adherence

### System Usage
- Regular updates
- Data backup
- Security protocols
- User training
- Performance monitoring

## Architecture

Refer to `Architecture.png` for a detailed view of:
- System components
- Data flow
- AWS service integration
- Security measures
- User interfaces

## Security Features

- Data encryption
- Access control
- Audit logging
- GDPR compliance
- Privacy protection

## Troubleshooting

Common issues and solutions:
- Document processing errors
- API rate limits
- Integration issues
- Data synchronization
- Authentication problems

## Support

For support:
- Check documentation
- Contact system admin
- Submit issue ticket
- Review FAQ
- Schedule training

## Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/YourFeature`)
3. Commit changes (`git commit -m 'Add YourFeature'`)
4. Push to branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.