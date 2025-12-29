import requests

API_KEY='ZOJ82H60E41M1PC4'
SERVER_URL='https://www.alphavantage.co/'

symbols = ['AAPL', 'GOOGL', 'MSFT', 'AMZN', 'TSLA']



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
            print(response.json())


get_stock_market_data()