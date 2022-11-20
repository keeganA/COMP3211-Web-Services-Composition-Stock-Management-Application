import requests, json

BASE = "http://127.0.0.1:5000/"

# Test that all accounts are listed
def checkAccountList():
    response = requests.get(BASE + "accounts")
    print(response.json())

# Test an account and its status is displayed
def checkAccountStatus(accountType):
    response = requests.get(BASE + "accounts/" + accountType)
    print(response.json())

# Test that an account can be added
def addAccount(accountType, status):
    response = requests.put(BASE + "accounts/" + accountType, json={"Account":accountType, "Status":status})
    checkAccountList()

# Test that an account can be removed 
def removeAccount(accountType):
    response = requests.delete(BASE + "accounts/" + accountType, json={"Account":accountType})
    checkAccountList()

# Test that an account status can be updated
def updateAccount(accountType, status):
    response = requests.patch(BASE + "accounts/" + accountType, json={"Account":accountType, "Status":status})
    checkAccountList()

# Run tests
checkAccountList()
#checkAccountStatus("ChildrensFund")
addAccount("Savings", "Open")
removeAccount("Business")
#updateAccount("Current", "Closed")
