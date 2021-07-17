import requests
from datetime import date, timedelta


#CHOOSE A STOCK TO TRACK
STOCK = "TSLA"

#GET NEWS API KEY
NEWS_API_KEY = "INSERT APIT KEY"
NEWS_API = "https://newsapi.org/v2/everything"
COMPANY_NAME = "TESLA"
last_month_date = date.today() - timedelta(days=25)

#GET FREE API KEY
STOCK_API_KEY = "INSERT API KEY"
STOCK_API = "https://www.alphavantage.co/query"

#GET THE DAILY DATA THAT RETURNS THE OPEN PRICE, HIGHEST PRICE, LOWEST PRICE AND CLOSING PRICE OF THE DAY.
STOCK_PARAMS = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY,
}

#NEWS PARAMETERS
NEWS_PARAMS = {
    "qInTitle": COMPANY_NAME,
    "from": last_month_date,
    "sortBy": "publishedAt",
    "apiKey": NEWS_API_KEY
}


stock_response = requests.get(STOCK_API, params=STOCK_PARAMS)
stock_response.raise_for_status()

stock_data = stock_response.json()["Time Series (Daily)"]
stock_data_list = [value for key, value in stock_data.items()]


#ACCESS YESTERDAY'S AND THE DAY BEFORE CLOSING PRICE
yesterdays_data = float(stock_data_list[0]['4. close'])
day_before_data = float(stock_data_list[1]['4. close'])

#GET THE POSITIVE DIFFERENCE BETWEEN THE DAY BEFORE DATA AND YESTERDAY'S DATA BY USING PYTHON'S ABS FUNCTION
percent_difference = round(abs((day_before_data / yesterdays_data) - 1) * 100)

percent_difference = ("%.2f" % percent_difference)
is_up = yesterdays_data > day_before_data

#REQUEST THE NEWS DATA
news_response = requests.get(NEWS_API, params=NEWS_PARAMS)
news_response.raise_for_status()
news_data = news_response.json()

#ACCESS THE TOP 3 LATEST NEWS ABOUT THE COMPANY
news = news_data['articles']
latest_news = news[:3]


#USE THESE VARIABLES AS THE CONTENT WHEN NOTIFYING THE USER
first_latest_news = f"Headline: {latest_news[0]['title']}\nBrief: {latest_news[0]['description']}\nURL: " \
                    f"{latest_news[0]['url']}\n"
second_latest_news = f"Headline: {latest_news[1]['title']}\nBrief: {latest_news[1]['description']}\nURL: " \
                     f"{latest_news[1]['url']}\n"
third_latest_news = f"Headline: {latest_news[2]['title']}\nBrief: {latest_news[2]['description']}\nURL: " \
                    f"{latest_news[2]['url']}\n"