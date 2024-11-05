# Amazon Bedrock Model Evaluator

A Python application for evaluating Amazon Bedrock models using Streamlit.

## Prerequisites

- Python 3.12+
- pip or conda for package management
- AWS credentials configured

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/Amazon-Bedrock-Model-Evaluator.git
cd Amazon-Bedrock-Model-Evaluator
```

2. Create and activate a virtual environment (recommended):
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On Unix or MacOS
source venv/bin/activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

## Environment Setup

Create a `.env` file in the root directory with your AWS credentials:
```
AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key
AWS_DEFAULT_REGION=your_region
```

## Running the Application

Start the Streamlit app:
```bash
streamlit run app.py
```

## Project Structure

- `app.py`: Main Streamlit application
- `evaluation_steps.py`: Contains evaluation logic
- `knowledge_base_fetcher.py`: Handles knowledge base operations
- `orchestrator.py`: Main orchestration logic
- `plotting_and_reporting.py`: Visualization and reporting utilities
- `pricing_calculator.py`: Cost calculation functions
- `text_extractor_and_summarizer.py`: Text processing utilities

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.