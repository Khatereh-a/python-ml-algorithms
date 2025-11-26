"""
Sentiment Analysis with Transformers
=====================================
A simple but powerful example of using pre-trained AI models for text sentiment analysis.

This script demonstrates:
- Loading a pre-trained sentiment analysis model from Hugging Face
- Analyzing sentiment of text (positive/negative)
- Batch processing multiple texts
- Visualizing results

Usage:
    python 01_sentiment_analysis.py
"""

from transformers import pipeline
import matplotlib.pyplot as plt


def analyze_sentiment(texts: list[str]) -> list[dict]:
    """
    Analyze sentiment of given texts using a pre-trained model.

    Args:
        texts: List of text strings to analyze

    Returns:
        List of dictionaries with 'label' and 'score' for each text
    """
    # Load pre-trained sentiment analysis pipeline
    # Uses 'distilbert-base-uncased-finetuned-sst-2-english' by default
    classifier = pipeline("sentiment-analysis")

    # Analyze all texts
    results = classifier(texts)
    return results


def visualize_results(texts: list[str], results: list[dict]) -> None:
    """Create a bar chart visualization of sentiment results."""

    labels = [r['label'] for r in results]
    scores = [r['score'] for r in results]
    colors = ['green' if l == 'POSITIVE' else 'red' for l in labels]

    # Truncate long texts for display
    display_texts = [t[:30] + '...' if len(t) > 30 else t for t in texts]

    plt.figure(figsize=(10, 6))
    bars = plt.barh(display_texts, scores, color=colors)

    # Add labels on bars
    for bar, label in zip(bars, labels):
        plt.text(bar.get_width() - 0.1, bar.get_y() + bar.get_height()/2,
                f'{label}', va='center', ha='right', color='white', fontweight='bold')

    plt.xlabel('Confidence Score')
    plt.title('Sentiment Analysis Results')
    plt.xlim(0, 1)
    plt.tight_layout()
    plt.savefig('sentiment_results.png', dpi=150)
    plt.show()
    print("\nChart saved to 'sentiment_results.png'")


def main():
    # Example texts to analyze
    sample_texts = [
        "I love this product! It's amazing and works perfectly.",
        "This is the worst experience I've ever had. Terrible service.",
        "The movie was okay, nothing special but not bad either.",
        "Absolutely fantastic! Would recommend to everyone.",
        "Very disappointed with the quality. Not worth the price.",
        "Great customer support, they solved my problem quickly!",
    ]

    print("=" * 60)
    print("SENTIMENT ANALYSIS WITH AI")
    print("=" * 60)
    print("\nLoading model (this may take a moment on first run)...\n")

    # Analyze sentiments
    results = analyze_sentiment(sample_texts)

    # Display results
    print("\nRESULTS:")
    print("-" * 60)
    for text, result in zip(sample_texts, results):
        sentiment = result['label']
        confidence = result['score']
        emoji = "✅" if sentiment == "POSITIVE" else "❌"
        print(f"{emoji} [{sentiment}] ({confidence:.2%})")
        print(f"   \"{text[:50]}{'...' if len(text) > 50 else ''}\"")
        print()

    # Visualize
    print("\nGenerating visualization...")
    visualize_results(sample_texts, results)

    # Interactive mode
    print("\n" + "=" * 60)
    print("TRY YOUR OWN TEXT")
    print("=" * 60)
    print("Enter text to analyze (or 'quit' to exit):\n")

    classifier = pipeline("sentiment-analysis")
    while True:
        user_input = input("> ")
        if user_input.lower() in ['quit', 'exit', 'q']:
            print("Goodbye!")
            break
        if user_input.strip():
            result = classifier(user_input)[0]
            emoji = "✅" if result['label'] == "POSITIVE" else "❌"
            print(f"   {emoji} {result['label']} (confidence: {result['score']:.2%})\n")


if __name__ == "__main__":
    main()
