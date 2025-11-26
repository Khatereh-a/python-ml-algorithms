# Python ML Algorithms

A collection of practical AI, Machine Learning, and LLM examples using Python.

## Topics Covered

| Category | Topics |
|----------|--------|
| **NLP & Text Analysis** | Sentiment analysis, text classification, tokenization |
| **Machine Learning** | Classification, clustering, regression |
| **Data Visualization** | Matplotlib, Pandas plotting, Seaborn |
| **Deep Learning** | Neural networks with PyTorch |
| **LLMs** | Working with large language models, prompt engineering |

## Quick Start

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/python-ml-algorithms.git
cd python-ml-algorithms
```

### 2. Create virtual environment
```bash
# Create
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (Linux/Mac)
source venv/bin/activate
```

### 3. Install dependencies
```bash
cd 01_sentiment_analysis
pip install -r requirements.txt
```

## Examples

### 01. Sentiment Analysis
Analyze text sentiment (positive/negative) using pre-trained transformer models.

```bash
cd 01_sentiment_analysis
python 01_sentiment_analysis.py
```

**What it does:**
- Loads a pre-trained DistilBERT model from Hugging Face
- Analyzes sentiment of sample texts with confidence scores
- Creates a visualization chart (saved as PNG)
- Provides interactive mode to analyze your own text

**Sample Output:**
```
POSITIVE (98.5%) - "I love this product! It's amazing!"
NEGATIVE (95.2%) - "This is the worst experience ever."
```

## Dependencies

| Package | Purpose |
|---------|---------|
| `transformers` | Pre-trained NLP models (Hugging Face) |
| `torch` | Deep learning framework |
| `scikit-learn` | Classical ML algorithms |
| `pandas` | Data manipulation |
| `numpy` | Numerical computing |
| `matplotlib` | Data visualization |

## Requirements

- Python 3.10+
- ~2GB disk space for model downloads (first run)
- Internet connection for downloading pre-trained models

## Project Structure

```
python-ml-algorithms/
├── 01_sentiment_analysis/
│   ├── 01_sentiment_analysis.py   # Main script
│   ├── requirements.txt           # Dependencies
│   └── REPORT.md                  # Development report
├── README.md                      # This file
└── .gitignore                     # Git ignore rules
```

## Coming Soon

- [ ] Text classification with custom datasets
- [ ] Image classification with CNNs
- [ ] Clustering algorithms (K-means, DBSCAN)
- [ ] Linear & logistic regression
- [ ] LLM prompt engineering examples
- [ ] RAG (Retrieval Augmented Generation)
- [ ] Fine-tuning models

## License

MIT License - feel free to use for learning and projects.
