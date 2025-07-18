This project uses NLP and sentiment analysis to enrich the Goodbooks-10k dataset, identify the mood of each book based on its title, and power a Flask web application for sentiment-based book recommendations.

🚀 Features
Load and preprocess books.csv from the Goodbooks-10k dataset.

Analyze book sentiment using a transformer model.

Assign each book a label: positive, neutral, or negative.

Save and use the enriched data in a Flask web app.

Filter books by sentiment and recommend mood-matching titles.

(Optional) Display book cover images via Open Library API.

📂 Dataset Used
Name: Goodbooks-10k

Columns: book_id, title, authors, average_rating, description, image_url, etc.

Location: books.csv

🤗 Sentiment Model
Model: cardiffnlp/twitter-roberta-base-sentiment

Type: RoBERTa transformer

Task: Sentiment classification (positive, neutral, negative)

