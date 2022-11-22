import yfinance as yf
from time import time 

start=time()
stock = yf.Ticker("Meta")
stockInfo = stock.info
end=time()
print(end-start)


def GetSummaryAndPrice():
        stockInput = input("Which stock would you want go get to know more about. Please enter the ticker symbol of the stock?")
        stock = yf.Ticker(stockInput)
        stockInfo = stock.info
        print("\nHere is some information about the stock: ", stockInfo["longBusinessSummary"])
        print("\nThe current price of the stock is: ", stockInfo["regularMarketPrice"])