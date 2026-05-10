from datetime import datetime
from textblob import TextBlob

print("=" * 40)
print("   Sentiment Analysis Tool")
print("=" * 40)

while True:
    text = input("\nEnter a sentence (or 'quit' to exit): ")

    if text.lower() == 'quit':
        print("Goodbye!")
        break

    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity

    if polarity > 0:
        sentiment = "Positive 😊"
    elif polarity < 0:
        sentiment = "Negative 😞"
    else:
        sentiment = "Neutral 😐"

    print(f"\nResult:")
    print(f"Sentiment   : {sentiment}")
    print(f"Polarity    : {polarity:.2f}  (-1 negative to +1 positive)")
    print(f"Subjectivity: {subjectivity:.2f}  (0 factual to 1 opinion)")
    print("-" * 40)

    with open("results.txt", "a") as f:
        f.write(f"\nDate       : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Text       : {text}\n")
        f.write(f"Sentiment  : {sentiment}\n")
        f.write(f"Polarity   : {polarity:.2f}\n")
        f.write(f"Subjectivity: {subjectivity:.2f}\n")
        f.write("-" * 40 + "\n")

print("\nResults saved to results.txt")