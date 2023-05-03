import requests
from flask import Flask, render_template

app = Flask(__name__)

API_KEY = ""
BASE_URL = "https://newsapi.org/v2/top-headlines"

def fetch_top_headlines(country="us", category="general"):
    params = {
        "country": country,
        "category": category,
        "apiKey": API_KEY,
    }
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        data = response.json()
        return data["articles"]
    else:
        print(f"Error {response.status_code}: Failed to fetch top headlines")
        return None

@app.route("/")
def index():
    articles = fetch_top_headlines()
    return render_template("index.html", articles=articles)

if __name__ == "__main__":
    app.run(debug=True)
