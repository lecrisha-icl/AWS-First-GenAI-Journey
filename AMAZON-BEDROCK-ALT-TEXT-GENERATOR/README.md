# AWS First GenAI Journey

![AWS Bedrock](https://img.shields.io/badge/AWS-Bedrock-orange)
![AWS CDK](https://img.shields.io/badge/AWS-CDK-blue)
![Python](https://img.shields.io/badge/Python-3.11-blue)
![License](https://img.shields.io/badge/License-Apache_2.0-green)

## 🎯 Overview

The AWS First GenAI Journey is a comprehensive solution that demonstrates how to build and deploy Generative AI applications on AWS. This repository provides ready-to-deploy CDK stacks and sample applications showcasing different use cases of Generative AI using Amazon Bedrock and other AWS services.

## 🚀 Quick Start

### Prerequisites

1. **AWS Account Setup**:
   - Active AWS Account
   - AWS CLI installed and configured
   - IAM user/role with appropriate permissions
   
2. **Development Environment**:
   - Python 3.11+ ([Download](https://www.python.org/downloads/))
   - Node.js 18+ ([Download](https://nodejs.org/))
   - AWS CDK CLI (`npm install -g aws-cdk`)
   - Git

### Local Environment Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/aws-samples/AWS-First-GenAI-Journey.git
   cd AWS-First-GenAI-Journey
   ```

2. **Set Up Python Virtual Environment**
   ```bash
   python -m venv .venv
   
   # Windows
   .venv\Scripts\activate
   
   # macOS/Linux
   source .venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## 📁 Repository Structure

```
AWS-First-GenAI-Journey/
├── infrastructure/             # CDK infrastructure code
├── src/                       # Application source code
│   ├── api/                   # API implementations
│   ├── layers/                # Lambda layers
│   └── tools/                 # Utility tools
├── test/                      # Test files
├── cdk.json                   # CDK configuration
└── README.md                  # Project documentation
```

## 💻 Available Demos

1. **Document Q&A**
   - Build a document Q&A system using Bedrock
   - Includes RAG (Retrieval-Augmented Generation) implementation
   - Supports PDF, TXT, and DOC formats

2. **Image Generation**
   - Generate images using Stable Diffusion
   - Custom prompt engineering
   - Image manipulation and editing

3. **Text Generation**
   - Text completion and generation
   - Custom prompt templates
   - Multiple model support

## 🏗️ Deployment

### CDK Deployment

1. **Bootstrap CDK** (if not already done)
   ```bash
   cdk bootstrap
   ```

2. **Deploy the Stack**
   ```bash
   cdk deploy
   ```

### Configuration

1. **Environment Variables**
   Copy `.env.example` to `.env` and update the values:
   ```bash
   cp .env.example .env
   ```

2. **AWS Region Configuration**
   Update the region in `cdk.json` if needed:
   ```json
   {
     "app": "python app.py",
     "region": "us-east-1"
   }
   ```

## 📊 Architecture

The solution is built using the following AWS services:

- **Amazon Bedrock**: For AI/ML model inference
- **Amazon S3**: For storing documents and artifacts
- **Amazon DynamoDB**: For metadata and session management
- **AWS Lambda**: For serverless compute
- **Amazon API Gateway**: For REST API endpoints
- **AWS CDK**: For infrastructure as code

## 🔧 Development

### Adding New Features

1. Create a new branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. Make your changes and commit:
   ```bash
   git add .
   git commit -m "Add: your feature description"
   ```

3. Push and create a pull request:
   ```bash
   git push origin feature/your-feature-name
   ```

### Running Tests

```bash
pytest test/
```

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for more details.

## 📝 License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

- Create a GitHub issue for bug reports and feature requests
- Contact AWS Support for AWS-related issues
- Check AWS Documentation for service-specific guidance

## 📚 Additional Resources

- [Amazon Bedrock Documentation](https://docs.aws.amazon.com/bedrock/)
- [AWS CDK Python Reference](https://docs.aws.amazon.com/cdk/api/v2/python/)
- [Generative AI on AWS](https://aws.amazon.com/generative-ai/)
- [AWS Solutions Architect Blog](https://aws.amazon.com/blogs/architecture/)

## 🔄 Updates and Maintenance

This repository is actively maintained. Please watch the repository for updates and check the [CHANGELOG](CHANGELOG.md) for version history.

## ⭐ Star History

If you find this project useful, please give it a star! Your support helps us continue developing and maintaining this resource.

## 📫 Contact

For any questions or feedback, please reach out to the AWS Solutions Architecture team or create an issue in this repository.