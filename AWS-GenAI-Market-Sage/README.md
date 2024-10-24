# AWS First GenAI Journey - Stock-Assistant

## Technical Guide: Stock-Assistant with Amazon Bedrock and Claude 3 Sonnet Model

### Overview

The **Stock-Assistant** demo leverages **Amazon Bedrock** and **Anthropic's Claude 3 Sonnet Model** using **Langchain** and **Streamlit**. This project demonstrates how to build and deploy an AI-driven assistant capable of interacting with stock-related data and assisting users in querying relevant information.

For detailed documentation, visit:
- [Amazon Bedrock Overview](https://aws.amazon.com/bedrock/)
- [Claude 3 Overview](https://www.anthropic.com/news/claude-3-family)

---

### Setup Instructions

#### 1. Install Python
Ensure Python is installed. Refer to the [official installation guide](https://docs.python-guide.org/starting/install3/linux/).

#### 2. Set Up a Python Virtual Environment
To avoid dependency issues, create a virtual environment:
```bash
# Install virtualenv if needed
pip install virtualenv

# Create a virtual environment
virtualenv venv

# Activate the virtual environment (Linux/Mac)
source venv/bin/activate

# (Windows)
venv\Scripts\activate
```

#### 3. Install AWS CLI
To configure and access AWS services (Amazon Bedrock), install the AWS CLI:
- [AWS CLI Quickstart](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-quickstart.html)

After installation, configure it with your AWS credentials:
```bash
aws configure
```

#### 4. Clone the Repository and Run the Application
```bash
# Clone the repository
git clone https://github.com/aws-samples/AWS-First-GenAI-Journey.git

# Change into the directory
cd AWS-First-GenAI-Journey/stock-assistant

# Install required dependencies
pip install -r requirements.txt

# Run the app using Streamlit
streamlit run Home.py --server.port 8501
```

Access the app at `http://localhost:8501`.

---

### Architecture

The Stock-Assistant is designed with modular components, focusing on scalability and ease of integration:
- **Amazon Bedrock**: AI model hosting and inference service.
- **Claude 3 Sonnet**: NLP model from Anthropic for interacting with users.
- **Langchain**: Framework for integrating AI models into applications.
- **Streamlit**: Frontend framework for creating interactive web applications.

![Architecture](./architecture.png)

---

### Learn More About Prompts and Claude 3

For more insights on prompt design and the Claude 3 model:
- [Prompt Design Guide](https://docs.anthropic.com/claude/docs/introduction-to-prompt-design)
- [Claude 3 Model Card](https://www-cdn.anthropic.com/de8ba9b01c9ab7cbabf5c33b80b7bbc618857627/Model_Card_Claude_3.pdf)

---

### Contributing

We welcome contributions! Please submit your pull requests to the [AWS First GenAI Journey repo](https://github.com/aws-samples/AWS-First-GenAI-Journey).