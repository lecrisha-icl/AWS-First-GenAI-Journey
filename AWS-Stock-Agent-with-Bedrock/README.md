# Technical Guide: Stock-Assistant with Amazon Bedrock and Claude 3 Sonnet Model

This repository is a part of AWS's Generative AI journey examples, based on the AWS official sample repository available at [AWS First GenAI Journey](https://github.com/aws-samples/AWS-First-GenAI-Journey). Below are the detailed steps for setting up the **Stock-Assistant** application using **Amazon Bedrock** and **Anthropic's Claude 3 Sonnet Model**.

---

## Overview

The **Stock-Assistant** project demonstrates how to deploy an AI-driven assistant for interacting with stock-related data using **Amazon Bedrock** for model inference and **Claude 3 Sonnet** for natural language processing, integrated with **Langchain** and **Streamlit** for smooth end-user interaction.

### Key Technologies:
- **Amazon Bedrock**: Managed service for foundational AI model deployment.
- **Anthropic Claude 3 Sonnet**: A cutting-edge NLP model for text generation and comprehension.
- **Langchain**: Framework to connect LLMs with other data or external services.
- **Streamlit**: Web app framework for creating interactive data-driven tools.

For more details on the core technologies, refer to the following links:
- [Amazon Bedrock](https://aws.amazon.com/bedrock/)
- [Claude 3](https://www.anthropic.com/news/claude-3-family)

---

## Setup Instructions

### 1. Install Python
Ensure Python 3 is installed in your system. Follow the official guide for setup:
- [Python Installation Guide](https://docs.python-guide.org/starting/install3/linux/)

### 2. Create a Python Virtual Environment
It's recommended to isolate dependencies by setting up a virtual environment.
```bash
# Install virtualenv if not installed
pip install virtualenv

# Create a virtual environment
virtualenv venv

# Activate the virtual environment
source venv/bin/activate   # For Linux/macOS
# OR
venv\Scripts\activate      # For Windows
```

### 3. Install AWS CLI
To interact with Amazon Bedrock, install the AWS Command Line Interface (CLI):
```bash
# Install AWS CLI (for Linux/macOS)
curl "https://awscli.amazonaws.com/AWSCLIV2.pkg" -o "AWSCLIV2.pkg"
sudo installer -pkg AWSCLIV2.pkg -target /

# Configure AWS CLI
aws configure
```

Refer to the [AWS CLI Quickstart Guide](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-quickstart.html) for more details.

### 4. Clone and Run the Stock-Assistant Application
```bash
# Clone the repository
git clone https://github.com/aws-samples/AWS-First-GenAI-Journey

# Change to the project directory
cd AWS-First-GenAI-Journey/stock-assistant

# Install dependencies
pip install -r requirements.txt

# Run the app using Streamlit
streamlit run Home.py --server.port 8501
```

The app should be accessible in your browser at `http://localhost:8501`.

---

## Architecture Overview

The Stock-Assistant uses a layered architecture designed for flexibility and scalability:

1. **User Interface (UI)**: Built using **Streamlit**, providing an interactive platform for users to query stock-related information.
2. **Application Layer**: Uses **Langchain** to manage interactions between the user input, data sources, and **Claude 3** model.
3. **Model Inference**: Leverages **Amazon Bedrock** to serve the **Claude 3 Sonnet** model from Anthropic for intelligent responses.

![Architecture](./architecture.png)

---

## Learn More

### Prompts and AI Model
Explore how to design prompts for effective interaction with **Claude 3** and learn more about the capabilities of the model:
- [Introduction to Prompt Design](https://docs.anthropic.com/claude/docs/introduction-to-prompt-design)
- [Claude 3 Model Card](https://www-cdn.anthropic.com/de8ba9b01c9ab7cbabf5c33b80b7bbc618857627/Model_Card_Claude_3.pdf)