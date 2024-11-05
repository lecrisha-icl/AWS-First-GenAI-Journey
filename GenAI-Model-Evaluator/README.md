# GenAI Model Evaluator

A comprehensive tool for evaluating and benchmarking Generative AI models, including performance metrics, cost analysis, and reporting capabilities.

## Project Structure

```
.
├── examples/                          # Example use cases
├── reports/                          # Generated evaluation reports
├── AnthropicTokenCounter.py         # Token counting utility
├── app.py                           # Main application
├── evaluation_steps.py              # Evaluation procedures
├── knowledge_base_fetcher.py        # Knowledge base management
├── orchestration_helper.py          # Orchestration utilities
├── orchestration_rag_helper.py      # RAG-specific helpers
├── orchestrator.py                  # Main orchestration logic
├── plotting_and_reporting.py        # Visualization utilities
├── pricing_calculator.py            # Cost analysis tools
└── text_extractor_and_summarizer.py # Text processing utilities
```

## Features

- Model performance evaluation
- Token usage tracking and analysis
- Cost calculation and optimization
- RAG (Retrieval-Augmented Generation) evaluation
- Automated reporting and visualization
- Knowledge base management
- Text extraction and summarization
- Comparative model analysis

## Prerequisites

- Python 3.12+
- Required Python packages (see requirements.txt)
- Access to GenAI models for evaluation
- Sufficient computational resources

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/GenAI-Model-Evaluator.git
cd GenAI-Model-Evaluator
```

2. Create virtual environment:
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

## Usage

### Basic Model Evaluation

```python
from evaluation_steps import evaluate_model

results = evaluate_model(
    model_name="model-name",
    test_cases=test_dataset,
    metrics=["accuracy", "latency", "token_usage"]
)
```

### Token Usage Analysis

```python
from AnthropicTokenCounter import count_tokens

token_count = count_tokens(
    text="Your text here",
    model="claude-3"
)
```

### Cost Calculation

```python
from pricing_calculator import calculate_cost

estimated_cost = calculate_cost(
    token_count=1000,
    model_name="model-name",
    operation_type="inference"
)
```

### Generate Reports

```python
from plotting_and_reporting import generate_report

report = generate_report(
    evaluation_results=results,
    report_type="comprehensive"
)
```

## Evaluation Metrics

- Response Quality
- Latency
- Token Efficiency
- Cost Effectiveness
- Knowledge Accuracy
- RAG Performance
- Error Rates
- Resource Usage

## Configuration

Create a `.env` file:
```
MODEL_API_KEY=your_api_key
REPORT_OUTPUT_DIR=./reports
ENABLE_DETAILED_LOGGING=true
```

## Report Types

1. Performance Reports
   - Response time analysis
   - Token usage statistics
   - Error rate tracking

2. Cost Analysis Reports
   - Per-request costs
   - Projected usage costs
   - Cost optimization recommendations

3. Quality Assessment Reports
   - Response accuracy
   - Knowledge retrieval effectiveness
   - Output consistency

## Orchestration

The orchestrator manages:
- Test case execution
- Resource allocation
- Error handling
- Result aggregation
- Report generation

## Best Practices

- Regular model evaluation
- Comprehensive test cases
- Consistent metrics tracking
- Cost monitoring
- Performance benchmarking

## Troubleshooting

Common issues and solutions:
- API rate limits
- Resource constraints
- Token counting accuracy
- Report generation errors

## Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/YourFeature`)
3. Commit changes (`git commit -m 'Add YourFeature'`)
4. Push to branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.