import requests
from tinydb import TinyDB
from datetime import datetime


# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=JPM&interval=5min&apikey=0AM4KRGJW335DO84'
headers = {
    "Accept": "application/json",
    "User-Agent": "MinhaAplicacao/1.0"
    }

params = {"currency": "USD"}

r = requests.get(url,headers=headers, params=params)
data = r.json()

print(data)
