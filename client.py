import requests, json
import yfinance as yf

BASE = "http://127.0.0.1:"

# Test that all accounts are listed
def checkAccountList():
    response = requests.get(BASE + "5000/accounts")
    print(response.json())

# Test an account and its status is displayed
def checkAccountStatus(accountType):
    response = requests.get(BASE + "5000/accounts/" + accountType)
    print(response.json())

# Test that an account can be added
def addAccount(accountType, status):
    response = requests.put(BASE + "5000/accounts/" + accountType, json={"Account":accountType, "Status":status})
    #checkAccountList()

# Test that an account can be removed 
def removeAccount(accountType):
    response = requests.delete(BASE + "5000/accounts/" + accountType, json={"Account":accountType})
    #checkAccountList()

# Test that an account status can be updated
def updateAccount(accountType, status):
    response = requests.put(BASE + "5000/accounts/" + accountType, json={"Account":accountType, "Status":status})
    #checkAccountList()


## Set of functions for the second web service


def getInfoForAccount(profile):#use to display all stocks owned by the user
    response = requests.get(BASE + "3000/profile/" + profile)
    print(response.json())

def addParticularStockAndQuantity(profile, stock, quantity):
    response = requests.put(BASE + "3000/profile/" + profile, json={"stock":stock, "quantity":quantity})
    #print(response.json())

def removeParticularStock(profile, stock):
    response = requests.delete(BASE + "3000/profile/" + profile, json={"stock":stock})
    print(response.json())

def UpdateParticularQuantityOfStock(profile, stock, quantity):
    response = requests.put(BASE + "3000/profile/" + profile, json={"stock":stock, "quantity":quantity})
    #print(response.json())





#####
def secondPage(profile):
    while(True):
        print("")
        print("1) Add stock and quantity ")
        print("2) Remove stock ")
        print("3) Change quantity of stock")
        print("4) View stocks owned")
        print("5) Get further information about a stock")
        print("6) Back to accounts page")

        option = int(input("\nChoose an Option\n"))    
    
        if option == 1:
            stock = input("What stock do you want to add?")
            quantity = int(input("How many?"))
            addParticularStockAndQuantity(profile,stock,quantity)

        elif option == 2:
            stock = input("What stock do you want to remove?")
            removeParticularStock(profile,stock)
        
        elif option == 3:
            stock = input("What stock's quantity would you like to update?")
            quantity = int(input("What quantity would you like to change it to??\n"))
            UpdateParticularQuantityOfStock(profile,stock, quantity)

        elif option == 4:
            getInfoForAccount(profile)

        elif option == 5:
            stockInput = input("Which stock would you want go get to know more about. Please enter the ticker symbol of the stock?")
            stock = yf.Ticker(stockInput)
            stockInfo = stock.info
            print("\nHere is some information about the stock: ", stockInfo["longBusinessSummary"])
            print("\nThe current price of the stock is: ", stockInfo["regularMarketPrice"])
            

        elif option == 6:
            firstPage()


def firstPage():
    checkAccountList()

    while(True):
        print("")
        print("1) Detailed view of specific account ")
        print("2) Check status of specfic account")
        print("3) Add new account")
        print("4) Remove specfic account")

        option = int(input("\nChoose an Option\n"))

        if option == 1:
            profile = input("What account do you want to view?")
            secondPage(profile)

        elif option == 2:#maybe show user the accounts available
            accountTypeToBeChecked = input("Which account do you want to check the status of?\n")
            checkAccountStatus(accountTypeToBeChecked)
        
        elif option == 3:
            accountType = input("What is the name of the account?\n")
            status = input("What is the status of the account (Open or Closed)?\n") 
            addAccount(accountType, status)

        elif option == 4:
            accountType = input("What is the name of the account you want to remove?\n")
            removeAccount(accountType)






firstPage()























