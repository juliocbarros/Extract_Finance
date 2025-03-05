import requests
from tinydb import TinyDB
from datetime import datetime


def extract_dados():
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=JPM&interval=5min&apikey=0AM4KRGJW335DO84'
    response = requests.get(url)
    dados = response.json()
    return dados


     