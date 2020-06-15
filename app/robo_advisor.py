import requests
import json
import os
import csv
import datetime
from dotenv import load_dotenv
import plotly
import plotly.graph_objs as go
import pandas

load_dotenv() #> loads contents of the .env file into the script's environment

def to_usd(my_price):
    return f"${my_price:,.2f}" #> $12,000.71

api_key = os.environ.get("ALPHAVANTAGE_API_KEY")

#input("ENTER TICKER HERE: ")

symbol = input("ENTER TICKER HERE: ")

request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}"

response = requests.get(request_url)

parsed_response = json.loads(response.text)

last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]

tsd = parsed_response["Time Series (Daily)"]

dates = list(tsd.keys()) 

latest_day = dates[0]

latest_close = tsd[latest_day]["4. close"]

high_prices = []
low_prices = []

for date in dates:
    high_price = tsd[date]["2. high"]
    low_price = tsd[date]["3. low"]
    high_prices.append(float(high_price))
    low_prices.append(float(low_price))

recent_high = max(high_prices)
recent_low = min(low_prices)

now = datetime.datetime.now()

csv_file_path = "data/prices.csv" # a relative filepath

csv_file_path = os.path.join(os.path.dirname(__file__), "../data/prices.csv")

csv_headers = ["timestamp", "open", "high", "low", "close", "volume"]

with open(csv_file_path, "w") as csv_file: # "w" means "open the file for writing"
    writer = csv.DictWriter(csv_file, fieldnames=csv_headers)
    writer.writeheader() # uses fieldnames set above
    for date in dates:
        daily_prices = tsd[date]
        writer.writerow({
        "timestamp": date, 
        "open": daily_prices["1. open"], 
        "high": daily_prices["2. high"],
        "low": daily_prices["3. low"],
        "close": daily_prices["4. close"],
        "volume": daily_prices["5. volume"]
    })

if float(latest_close) <= float(recent_low*1.1):
    recommendation = "BUY IT WARREN"
    reason = "EQUITY SALE ON ISLE FIVE"

if float(latest_close) >= float(recent_high*.8):
    recommendation = "SELL IT MR. BUFFETT"
    reason = "SKY HIGH, CASH IN"

if float(recent_low*1.1) < float(latest_close) < float(recent_high*.8):
    recommendation = "HOLD IT MR. BUFFETT"
    reason = "NOTHING INTERESTING TO SEE HERE, KEEP HOLDING"

print("-------------------------")
print(f"SELECTED SYMBOL: {symbol}")
print("-------------------------")
print("REQUESTING STOCK MARKET DATA")
print("REQUEST AT:", now.strftime("%Y-%m-%d %H:%M %p")) #can I change this from 24 hour clock?
print("-------------------------")
print(f"LATEST DAY: {last_refreshed}")
print(f"LATEST CLOSE: {to_usd(float((latest_close)))}")
print(f"RECENT HIGH: {to_usd(float((recent_high)))}") # 100 day max high
print(f"RECENT LOW: {to_usd(float((recent_low)))}") # 100 day min low
print("-------------------------")
print(f"RECOMMENDATION: {recommendation}")
print(f"RECOMMENDATION REASON: {reason}")
print("-------------------------")
print(f"WRITING DATA TO CSV: {csv_file_path}")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")

x = (dates)
y = (high_prices)

plotly.offline.plot({
    "data": [go.Scatter(x = x, y = y)],
    "layout": go.Layout(title=f"Daily Highs for {symbol}")
}, auto_open=True)
