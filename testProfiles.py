import requests, json
from time import time 


#data = {"name":"tutorialOf","views":55,"likes":10}
# response = requests.put(BASE + "/accounts/1", json = data )
#print(response.json())

# input()

BASE = "http://127.0.0.1:3000"




def getInfoForAccount(profile):#use to display all stocks owned by the user
    response = requests.get(BASE + "/profile/" + profile)
    #print(response.json())

def addParticularStockAndQuantity(profile, stock, quantity):
    response = requests.put(BASE + "/profile/" + profile, json={"stock":stock, "quantity":quantity})
    #print(response.json())

def removeParticularStock(profile, stock):
    response = requests.delete(BASE + "/profile/" + profile, json={"stock":stock})
    #print(response.json())

def UpdateParticularQuantityOfStock(profile, stock, quantity):
    response = requests.put(BASE + "/profile/" + profile, json={"stock":stock, "quantity":quantity})
    #print(response.json())


start =time()
getInfoForAccount("Current")
addParticularStockAndQuantity("Current","IBM", 9)
removeParticularStock("Current", "Meta")
UpdateParticularQuantityOfStock("Current","Amazon",50)
finish = time()

print(finish-start)