import requests, json
import time
import numpy as np
import matplotlib.pyplot as plt

BASE = "http://127.0.0.1:3020/"

# Test that all accounts are listed
def checkAccountList():
    response = requests.get(BASE + "accounts")
    return response.json()

# Test an account and its status is displayed
def checkAccountStatus(accountType):
    response = requests.get(BASE + "accounts/" + accountType)
    return response.json()

# Test that an account can be added
def addAccount(accountType, status):
    response = requests.put(BASE + "accounts/" + accountType, json={"Account":accountType, "Status":status})

# Test that an account can be removed 
def removeAccount(accountType):
    response = requests.delete(BASE + "accounts/" + accountType, json={"Account":accountType})

# Test that an account status can be updated
def updateAccount(accountType, status):
    response = requests.put(BASE + "accounts/" + accountType, json={"Account":accountType, "Status":status})

# Run tests
def runTests():
    # Read account list 
    checkAccountList()
    # Read account status
    checkAccountStatus("ChildrensFund")
    # Create account 
    addAccount("Savings", "Open")
    # Update account 
    updateAccount("Current", "Closed")
    # Delete account 
    removeAccount("Business")

# Calculate service invocation tasks
def calculateTime():
    n = 10
    times = []
    for i in range(0, n):
        st = time.time()
        print("Test Number ", i)
        runTests()
        end = time.time()
        time_elapsed = end - st
        times.append(time_elapsed)
        time.sleep(1)

        # Restore list to original state
        addAccount("Business", "Open") 
        updateAccount("Current", "Open")
        removeAccount("Savings")

    total_time = sum(times)
    average_time = total_time/n
    std_dev_time = np.std(times)
    print("The total time taken for 10 workflow invocations is:", total_time.__round__(4))
    print("On average each invocation took:", average_time.__round__(4))
    print("The standard deviation for the 10 workflow invocations is:", std_dev_time.__round__(4))

    x = list(range(0,10))
    y = times
    plt.title("Service Invocation Time") 
    plt.xlabel("Service Invocation Number (n)") 
    plt.ylabel("Execution Time (s)") 
    plt.plot(x,y) 
    plt.xticks(ticks=x)
    plt.show()

# Client
def client():
    print("\n--- START CLIENT TESTING ---\n")
    print("\nClient reads the list of accounts")
    accounts = checkAccountList()
    for key, value in accounts.items():
        print(key,':', value)
    print("\nClient can read the status of an specific account")
    account = checkAccountStatus("ChildrensFund")
    print('Account Name:', account[0])
    print('Account Status:', account[1])
    print("\nThe client can create a new account.\nHere the client creates the account Savings with a status of 'Open'")
    addAccount("Savings", "Open")
    accounts = checkAccountList()
    for key, value in accounts.items():
        print(key,':', value)
    print("\nThe client can update an account\nHere the client updates their Current account with a status of 'Closed'")
    updateAccount("Current", "Closed")
    accounts = checkAccountList()
    for key, value in accounts.items():
        print(key,':', value)
    print("\nFinally, the client can delete an account\nHere the client deletes their Business account")
    removeAccount("Business")
    accounts = checkAccountList()
    for key, value in accounts.items():
        print(key,':', value)

    print("\n--- CLIENT TESTING COMPLETE ---\n")

#calculateTime()
client()