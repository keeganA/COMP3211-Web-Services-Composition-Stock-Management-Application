import yfinance as yf
from time import time 

# Check service invocation time
start=time()
stock = yf.Ticker("Meta")
stockInfo = stock.info
end=time()
time_taken = end - start
print('Invocation time taken: ', time_taken)

# Client for testing External REST API
def GetSummaryAndPrice():
        stockInput = input("Which stock would you want go get to know more about. Please enter the ticker symbol of the stock?")
        stock = yf.Ticker(stockInput)
        stockInfo = stock.info
        print("\nHere is some information about the stock: ", stockInfo["longBusinessSummary"])
        print("\nThe current price of the stock is: ", stockInfo["regularMarketPrice"])

# Run client test
GetSummaryAndPrice()
