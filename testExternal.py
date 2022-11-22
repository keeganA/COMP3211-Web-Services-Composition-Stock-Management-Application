import yfinance as yf
from time import time 

start=time()
stock = yf.Ticker("Meta")
stockInfo = stock.info
end=time()
print(end-start)
