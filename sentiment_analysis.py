from textblob import TextBlob

def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

reviews = [
    "This product is amazing and works great!",
    "Terrible experience, very disappointed.",
    "It is okay, nothing special.",
    "Absolutely love this! Best purchase ever.",
    "Worst product I have ever bought.",
    "Average quality, does the job.",
    "Highly recommend this to everyone!",
    "Not worth the money at all."
]

print("Sentiment Analysis Results")
print("-" * 40)
for review in reviews:
    sentiment = analyze_sentiment(review)
    print(f"Review: {review[:40]}...")
    print(f"Sentiment: {sentiment}")
    print()
