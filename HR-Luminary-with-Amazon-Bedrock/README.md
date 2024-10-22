# HR Luminary

## Overview
**HR Luminary** is an AI-powered recruitment assistant that enhances and streamlines the recruitment process. Built with Amazon Bedrock and Anthropic Claude models, integrated via LangChain, this project delivers capabilities like advanced resume screening, candidate evaluation, and interview assistance. The goal is to demonstrate how AI can improve HR decision-making and efficiency.

For details on the underlying technologies, visit:
- [Amazon Bedrock](https://aws.amazon.com/bedrock/)
- [Anthropic Claude](https://www.anthropic.com/index/claude-2)

## Setup Guide

### Prerequisites
Ensure you have the following before setting up:
- **Python** installed ([Installation Guide](https://docs.python-guide.org/starting/install3/linux/)).
- **AWS CLI** installed and configured ([Quickstart Guide](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-quickstart.html)).
- An **AWS Account** with Amazon Bedrock access.

### Step 1: Python Virtual Environment Setup
Create and activate a Python virtual environment to manage dependencies.

1. Run the following commands:
   ```bash
   python3 -m venv hr-luminary-env
   source hr-luminary-env/bin/activate
   ```

### Step 2: Clone the Repository
Clone the HR Luminary repository.

```bash
git clone https://github.com/aws-samples/AWS-First-GenAI-Journey
cd AWS-First-GenAI-Journey
```

### Step 3: Install Dependencies
Install all required dependencies using `requirements.txt`.

```bash
pip install -r requirements.txt
```

### Step 4: AWS CLI Configuration
Ensure AWS CLI is configured with valid credentials.

```bash
aws configure
```
Input your AWS Access Key, Secret Key, Region (`us-west-2` recommended), and Output format.

### Step 5: Running the Application
Start the Streamlit application to interact with HR Luminary.

```bash
streamlit run Home.py --server.port 8080
```
Access the app by navigating to `http://localhost:8080` in your browser.

## Architecture
HR Luminary's architecture integrates AI models with a user-friendly interface for effective recruitment workflows.

![Architecture](./Architecture.png)

## Learn More About Prompt Design
To enhance the model's efficiency, learn about prompt design [here](https://docs.anthropic.com/claude/docs/introduction-to-prompt-design).

## Contributing
We welcome contributions! Here's how to get started:

1. **Fork the Repository** on GitHub.
2. **Create a Branch** for your feature or fix:
   ```bash
   git checkout -b feature-name
   ```
3. **Make Your Changes**, then commit:
   ```bash
   git add .
   git commit -m "Brief description of changes"
   ```
4. **Push to Your Branch**:
   ```bash
   git push origin feature-name
   ```
5. **Submit a Pull Request** with details on your changes.

## License
This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.