import requests

#CHOOSE A STOCK TO TRACK
STOCK = "TSLA"

#GET FREE API KEY
STOCK_API_KEY = "INSERT API KEY"
STOCK_API = "https://www.alphavantage.co/query"

#GET THE DAILY DATA THAT RETURNS THE OPEN PRICE, HIGHEST PRICE, LOWEST PRICE AND CLOSING PRICE OF THE DAY.
STOCK_PARAMS = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY,
}

stock_response = requests.get(STOCK_API, params=STOCK_PARAMS)
stock_response.raise_for_status()

stock_data = stock_response.json()["Time Series (Daily)"]
stock_data_list = [value for key, value in stock_data.items()]