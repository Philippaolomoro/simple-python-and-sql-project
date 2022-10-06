import requests
import os
from dotenv import load_dotenv
load_dotenv()

def get_data():
    api_key = os.getenv("API_KEY")
    urls = [
        "https://finnhub.io/api/v1/quote?symbol=AAPL",
        "https://finnhub.io/api/v1/quote?symbol=AMZN",
        "https://finnhub.io/api/v1/quote?symbol=NFLX",
        "https://finnhub.io/api/v1/quote?symbol=META",
        "https://finnhub.io/api/v1/quote?symbol=GOOG"
    ]
    headers = {
      'Accept': 'application/json',
      'Content-Type': 'application/json',
      'X-Finnhub-Token': api_key
    }
    responses = []
    for url in urls:
        response = requests.request("GET", url, headers=headers)
        json_response = response.json()
        responses.append(json_response)
    return responses
