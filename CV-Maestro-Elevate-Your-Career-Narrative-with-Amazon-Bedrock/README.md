
# HR Luminary

## Overview
**HR Luminary** is an AI-powered recruitment assistant designed to streamline and enhance the recruitment process. This project leverages Amazon Bedrock and the Anthropic Claude model, integrated with the LangChain library, to offer advanced capabilities in candidate evaluation, resume screening, and interview assistance. HR Luminary demonstrates how AI can enhance efficiency and decision-making in human resources.

For more information on the core technologies, refer to:
- [Amazon Bedrock](https://aws.amazon.com/bedrock/)
- [Anthropic Claude](https://www.anthropic.com/index/claude-2)

## Setup Guide

### Prerequisites
Before setting up HR Luminary, ensure the following requirements are met:
- **Python 3.x** installed on your system. Follow instructions [here](https://docs.python-guide.org/starting/install3/linux/).
- **AWS CLI** installed and configured. Follow the quickstart guide [here](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-quickstart.html).
- An **AWS account** to access Amazon Bedrock.

### Step 1: Set Up a Python Virtual Environment
To avoid dependency conflicts, it's recommended to create a virtual environment.

1. Open a terminal.
2. Run the following commands to create and activate a virtual environment:
   ```bash
   python3 -m venv hr-luminary-env
   source hr-luminary-env/bin/activate
   ```

### Step 2: Clone the Repository
Clone the HR Luminary repository to your local environment.

1. Run the following commands:
   ```bash
   git clone https://github.com/aws-samples/AWS-First-GenAI-Journey
   cd AWS-First-GenAI-Journey
   ```

### Step 3: Install Dependencies
Install the necessary Python dependencies listed in `requirements.txt`.

1. Ensure the virtual environment is active.
2. Run:
   ```bash
   pip install -r requirements.txt
   ```

### Step 4: Configure AWS Credentials
Ensure your AWS CLI is properly configured to access Amazon Bedrock services.

1. Run:
   ```bash
   aws configure
   ```
2. Provide your AWS Access Key, Secret Key, Region, and Output format.

### Step 5: Run the Application
Start the HR Luminary application with Streamlit.

1. Run:
   ```bash
   streamlit run Home.py --server.port 8080
   ```
2. Open your browser and go to `http://localhost:8080` to access the application.

## Architecture
The HR Luminary architecture integrates AI models with a user-friendly interface to facilitate recruitment management. Here's a high-level architecture diagram:

![Architecture](./Architecture.png)

## Prompt Design Guide
For improved efficiency in AI-driven recruitment tasks, explore prompt design best practices [here](https://docs.anthropic.com/claude/docs/introduction-to-prompt-design).

## Contributing
We welcome contributions! To contribute:

1. **Fork the repository** on GitHub.
2. **Create a new branch** for your feature or bug fix:
   ```bash
   git checkout -b feature-or-bugfix-name
   ```
3. **Make your changes** and commit them:
   ```bash
   git add .
   git commit -m "Description of your changes"
   ```
4. **Push your changes**:
   ```bash
   git push origin feature-or-bugfix-name
   ```
5. **Open a Pull Request** on GitHub, detailing your changes.

## License
HR Luminary is licensed under the MIT License. See the [LICENSE](./LICENSE) file for more details.
