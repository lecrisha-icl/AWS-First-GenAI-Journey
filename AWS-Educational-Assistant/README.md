# AWS Educational Assistant: Technical Overview

The **AWS Educational Assistant** project demonstrates the integration of Amazon Bedrock and Anthropic's Claude 3 Sonnet model. This repository showcases how these services, combined with Langchain and a Streamlit web interface, can be leveraged to build an educational assistant application. This guide provides step-by-step instructions for deploying and running the project.

---

## Key Features

1. **Amazon Bedrock Integration**:
   - Utilizes Amazon Bedrock for scalable access to advanced foundation models like Claude 3 in a serverless environment.
   
2. **Anthropic Claude 3 Sonnet**:
   - Employs Claude 3 Sonnet for natural language understanding and generation, supporting educational use cases.

3. **Langchain Integration**:
   - Integrates Langchain to enable chaining of complex workflows and automated responses based on natural language prompts.

4. **Streamlit Web Interface**:
   - Offers an interactive, real-time user interface built with Streamlit for user interaction with the assistant.

---

## Prerequisites

1. **Python (version 3.8 or later)**
2. **AWS CLI** (configured for Amazon Bedrock access)
3. **Git** (to clone the repository)

---

## Step-by-Step Setup Guide

### 1. Install Python

Ensure that Python is installed on your system. Follow the appropriate installation guide:
- [Python Installation Guide](https://docs.python-guide.org/starting/install3/linux/)

Verify the installation by running:
```bash
python3 --version
```

### 2. Set Up a Python Virtual Environment

To prevent dependency conflicts, create a Python virtual environment:
```bash
python3 -m venv educational_assistant_env
source educational_assistant_env/bin/activate  # For Linux/Mac
# or
.\educational_assistant_env\Scripts\activate   # For Windows
```

### 3. Install and Configure AWS CLI

You will need the AWS CLI to authenticate and interact with Amazon Bedrock. Follow this guide to install AWS CLI:
- [AWS CLI Installation Guide](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)

After installation, configure the AWS CLI by running:
```bash
aws configure
```

Ensure you use a region that supports Amazon Bedrock (e.g., `us-west-2`).

### 4. Clone the AWS Educational Assistant Repository

Clone this project repository from GitHub:
```bash
git clone https://github.com/aws-samples/AWS-First-GenAI-Journey
cd AWS-First-GenAI-Journey
```

### 5. Install Project Dependencies

Install the required Python packages by running:
```bash
pip install -r requirements.txt
```

This installs necessary libraries like `streamlit`, `boto3`, `langchain`, and more.

### 6. Run the Streamlit Application

Launch the Streamlit application:
```bash
streamlit run Home.py --server.port 8080
```

The application will run on port `8080`. You can access it by opening `http://localhost:8080` in your web browser.

---

## Additional Resources

- **Amazon Bedrock Documentation**:
  - [Amazon Bedrock](https://aws.amazon.com/bedrock/)
- **Prompt Engineering Guide**:
  - [Introduction to Prompt Design](https://docs.anthropic.com/claude/docs/introduction-to-prompt-design)
- **Claude 3 Model Card**:
  - [Claude 3 Model Card](https://www-cdn.anthropic.com/de8ba9b01c9ab7cbabf5c33b80b7bbc618857627/Model_Card_Claude_3.pdf)