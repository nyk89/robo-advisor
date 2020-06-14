import requests
import json

#
# INFO INPUTS
#

request_url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=demo"

response = requests.get(request_url)
#
#
#

parsed_response = json.loads(response.text)

last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]


tsd = parsed_response["Time Series (Daily)"]

dates = list(tsd.keys()) # to do make sorted list so most recent date is first

latest_day = dates[0]

latest_close = tsd[latest_day]["4. close"]


# high_prices = [10, 20, 30, 5]
# recent_high = max(high_prices)


high_prices = []
low_prices = []

for date in dates:
    high_price = tsd[date]["2. high"]
    low_price = tsd[date]["3. low"]
    high_prices.append(float(high_price))
    low_prices.append(float(low_price))

recent_high = max(high_prices)
recent_low = min(low_prices)

# print(type(response)) # <class 'requests.models.Response'>
# print(response.status_code) #200
# print(response.text)



import datetime
now = datetime.datetime.now()

def to_usd(my_price):
    return f"${my_price:,.2f}" #> $12,000.71

print("-------------------------")
print("SELECTED SYMBOL: XYZ")
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT:", now.strftime("%Y-%m-%d %H:%M %p")) #can I change this from 24 hour clock?
print("-------------------------")
print(f"LATEST DAY: {last_refreshed}")
print(f"LATEST CLOSE: {to_usd(float((latest_close)))}")
print(f"RECENT HIGH: {to_usd(float((recent_high)))}") # 100 day max high
print(f"RECENT LOW: {to_usd(float((recent_low)))}") # 100 day min low
print("-------------------------")
print("RECOMMENDATION: BUY!")
print("RECOMMENDATION REASON: TODO")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")