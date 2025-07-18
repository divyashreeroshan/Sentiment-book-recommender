from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Load data with sentiment column
df = pd.read_csv("books_with_sentiment.csv")

@app.route("/")
def index():
    query = request.args.get("query", "").lower()
    sentiment_filter = request.args.get("sentiment", "").lower()

    filtered_df = df.copy()

    if query:
        filtered_df = filtered_df[filtered_df["title"].str.lower().str.contains(query)]

    if sentiment_filter in ["positive", "neutral", "negative"]:
        filtered_df = filtered_df[filtered_df["sentiment"].str.lower() == sentiment_filter]

    books = filtered_df.to_dict(orient="records")
    return render_template("index.html", books=books, query=query, sentiment=sentiment_filter)

if __name__ == "__main__":
    app.run(debug=True)
