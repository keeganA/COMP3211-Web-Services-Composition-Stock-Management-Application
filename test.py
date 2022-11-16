import requests, json


#data = {"name":"tutorialOf","views":55,"likes":10}
# response = requests.put(BASE + "/accounts/1", json = data )
#print(response.json())

# input()

BASE = "http://127.0.0.1:5000"




def getInfoForAccount(profile):#use to display all stocks owned by the user
    response = requests.get(BASE + "/accounts/" + profile)
    print(response.json())

def addParticularStockAndQuantity(profile, stock, quantity):
    response = requests.put(BASE + "/accounts/" + profile, json={"stock":stock, "quantity":quantity})
    #print(response.json())

def removeParticularStock(profile, stock):
    response = requests.delete(BASE + "/accounts/" + profile, json={"stock":stock})
    print(response.json())

def UpdateParticularQuantityOfStock(profile, stock, quantity):
    response = requests.put(BASE + "/accounts/" + profile, json={"stock":stock, "quantity":quantity})
    #print(response.json())



getInfoForAccount("jim")
input()
addParticularStockAndQuantity("jim","IBM", 9)
input()
getInfoForAccount("jim")
input()
removeParticularStock("jim", "Meta")
input()
getInfoForAccount("jim")
UpdateParticularQuantityOfStock("jim","Amazon",50)
input()
getInfoForAccount("jim")