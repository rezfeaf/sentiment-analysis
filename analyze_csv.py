import pandas as pd
from textblob import TextBlob

print("=" * 40)
print("   Bulk Sentiment Analysis")
print("=" * 40)

df = pd.read_csv("sentences.csv")

results = []

for text in df["text"]:
    blob = TextBlob(str(text))
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity

    if polarity > 0:
        sentiment = "Positive"
    elif polarity < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    results.append({
        "text": text,
        "sentiment": sentiment,
        "polarity": round(polarity, 2),
        "subjectivity": round(subjectivity, 2)
    })

results_df = pd.DataFrame(results)

print(results_df.to_string(index=False))

results_df.to_csv("analyzed_results.csv", index=False)
print("\nSaved to analyzed_results.csv")

counts=results_df["sentiment"].value_counts()

print("\n" + "=" * 40)
print("   Summary")
print("=" * 40)
print(f"Positive  : {counts.get('Positive', 0)}")
print(f"Negative  : {counts.get('Negative', 0)}")
print(f"Neutral   : {counts.get('Neutral', 0)}")
print(f"Avg Polarity: {results_df['polarity'].mean():.2f}")
print("=" * 40)