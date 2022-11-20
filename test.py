import requests, json


#data = {"name":"tutorialOf","views":55,"likes":10}
# response = requests.put(BASE + "/accounts/1", json = data )
#print(response.json())

# input()

BASE = "http://127.0.0.1:3000"




def getInfoForAccount(profile):#use to display all stocks owned by the user
    response = requests.get(BASE + "/profile/" + profile)
    print(response.json())

def addParticularStockAndQuantity(profile, stock, quantity):
    response = requests.put(BASE + "/profile/" + profile, json={"stock":stock, "quantity":quantity})
    print(response.json())

def removeParticularStock(profile, stock):
    response = requests.delete(BASE + "/profile/" + profile, json={"stock":stock})
    print(response.json())

def UpdateParticularQuantityOfStock(profile, stock, quantity):
    response = requests.put(BASE + "/profile/" + profile, json={"stock":stock, "quantity":quantity})
    print(response.json())



getInfoForAccount("Current")
input()
addParticularStockAndQuantity("Current","IBM", 9)
input()
getInfoForAccount("Current")
input()
removeParticularStock("Current", "Meta")
input()
getInfoForAccount("Current")
UpdateParticularQuantityOfStock("Current","Amazon",50)
input()
getInfoForAccount("Current")