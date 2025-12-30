
import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('STOCK_MARKET_API_KEY', 'your_default_api_key_here')
SERVER_URL='https://www.alphavantage.co/'

symbols = ['AAPL', 'GOOGL', 'MSFT', 'AMZN', 'TSLA', 'FB', 'NVDA', 'JPM', 'V', 'DIS', 'NFLX', 'ADBE', 'PYPL', 'INTC', 'CSCO', 'CMCSA', 'PEP', 'KO', 'NKE', 'WMT', 'BABA', 'ORCL', 'SAP', 'CRM', 'ABNB', 'UBER', 'LYFT', 'SQ', 'TWTR', 'SNAP', 'ZM', 'SHOP', 'SPOT', 'DOCU', 'ROKU', 'ETSY', 'CRWD', 'OKTA', 'ZS', 'DDOG', 'NET', 'FSLY', 'PLTR', 'AI', 'MDB', 'NOW', 'WORK', 'TEAM', 'DASH', 'RBLX', 'IBM']



def get_stock_market_data():
    while True:
        print("--------------------------------------------------------------------------------------")
        print("Available stock symbols:", symbols)
        print("--------------------------------------------------------------------------------------")
        symbol = input("Enter the valid stock symbol from the list (or type 'exit' to quit): ")
        print("--------------------------------------------------------------------------------------")
        url = SERVER_URL+'query?function=TIME_SERIES_DAILY&symbol='+symbol+'&apikey='+API_KEY
        print(url)
        if symbol.lower() == 'exit':
            print("Exiting the program.")
            break
        if symbol not in symbols:
            print("Invalid symbol. Please choose from the available symbols:", symbols)
            continue
        if symbol in symbols:
            url = SERVER_URL+'query?function=TIME_SERIES_DAILY&symbol='+symbol+'&apikey='+API_KEY
            response = requests.get(url=url)
            print("Status Code:", response.status_code)
            data = response.json()
            if "Time Series (Daily)" in data:
                time_series = data["Time Series (Daily)"]
                latest_date = sorted(time_series.keys(), reverse=True)[0]
                latest_data = time_series[latest_date]
                print(f"Stock data for {symbol} on {latest_date}:")
                print(f"  Open: {latest_data['1. open']}")
                print(f"  High: {latest_data['2. high']}")
                print(f"  Low: {latest_data['3. low']}")
                print(f"  Close: {latest_data['4. close']}")
                print(f"  Volume: {latest_data['5. volume']}")
            else:
                print("Error fetching data for symbol:", symbol)
get_stock_market_data()