# Amazon Bedrock Alt Text Generator

![Python](https://img.shields.io/badge/Python-3.12-blue)
![AWS](https://img.shields.io/badge/AWS-Bedrock-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-1.30-red)

## 🎯 Overview

A simple Streamlit application that uses Amazon Bedrock's AI capabilities to generate alternative text descriptions for images. This tool helps improve accessibility by providing AI-generated descriptions for uploaded images.

## ⚡️ Quick Start

### Prerequisites

- Python 3.12+ ([Download](https://www.python.org/downloads/))
- AWS Account with Bedrock access
- AWS CLI installed and configured

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repository-url>
   cd Amazon-Bedrock-Alt-Text-Generator
   ```

2. **Create and activate virtual environment**
   ```bash
   # Create virtual environment
   python -m venv streamlit_env

   # Windows
   streamlit_env\Scripts\activate

   # macOS/Linux
   source streamlit_env/bin/activate
   ```

3. **Install required packages**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   # Create .env file
   cp .env.example .env

   # Update .env with your AWS credentials
   AWS_ACCESS_KEY_ID=your_access_key
   AWS_SECRET_ACCESS_KEY=your_secret_key
   AWS_DEFAULT_REGION=your_region
   ```

5. **Run the application**
   ```bash
   streamlit run app.py
   ```

## 📁 Project Structure
```
.
├── app.py                  # Main Streamlit application
├── files/                  # File upload directory
├── images/                 # Static image assets
├── streamlit_env/          # Virtual environment
├── .env                    # Environment variables
├── .gitignore             # Git ignore file
├── requirements.txt        # Project dependencies
└── README.md              # Documentation
```

## 📝 Requirements

Main dependencies:
```txt
streamlit==1.30.0
boto3==1.34.0
python-dotenv==1.0.0
Pillow==10.1.0
```

## 🔑 AWS Configuration

1. **Configure AWS Credentials**
   - Create an IAM user with Bedrock access
   - Configure AWS CLI:
     ```bash
     aws configure
     ```
   - Or set environment variables in `.env`

2. **Enable Bedrock Model Access**
   - Go to AWS Console > Bedrock
   - Enable required model access in Model Access settings

## 💡 Usage

1. Start the app:
   ```bash
   streamlit run app.py
   ```

2. Open web browser:
   - Local URL: http://localhost:8501
   - Network URL: http://192.168.x.x:8501

3. Upload an image and wait for the AI-generated description

## ❗ Common Issues

1. **AWS Credentials Error**
   - Verify AWS credentials in `.env`
   - Check AWS CLI configuration
   - Ensure IAM user has Bedrock access

2. **Import Errors**
   - Confirm all dependencies are installed:
     ```bash
     pip install -r requirements.txt
     ```

3. **Streamlit Port Issues**
   - Change port if 8501 is in use:
     ```bash
     streamlit run app.py --server.port 8502
     ```

## 📫 Support

- Create an issue for bug reports or features
- Check AWS Bedrock documentation for service issues
- Review Streamlit docs for framework questions

## 📜 License

This project is under the MIT License. See LICENSE file for details.