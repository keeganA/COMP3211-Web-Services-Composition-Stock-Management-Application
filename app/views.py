from flask import Flask
from flask import render_template, flash, request, redirect, url_for, session
from app import app
from .forms import *
import os
import requests, json
import yfinance as yf
from flask import Markup

BASE = "http://127.0.0.1:"


"""

Web Service Functions

"""

## Set of functions for the first web service
def AccountList():
    response = requests.get(BASE + "3020/accounts")
    accounts = response.json()
    account_names = list(accounts.keys())
    account_statuses = list(accounts.values())
    return account_names, account_statuses

def addAnAccount(accountType, status):
    response = requests.put(BASE + "3020/accounts/" + accountType, json={"Account":accountType, "Status":status})

def removeAnAccount(accountType):
    response = requests.delete(BASE + "3020/accounts/" + accountType, json={"Account":accountType})

def updateAnAccount(accountType, status):
    response = requests.put(BASE + "3020/accounts/" + accountType, json={"Account":accountType, "Status":status})

## Set of functions for the second web service
def getInfoForAccount(profile):#use to display all stocks owned by the user
    response = requests.get(BASE + "3000/profile/" + profile)
    try:
        response.json()
    except ValueError as e:
        return 'Oops this Account is Closed!'
    profiles = response.json()
    profile_stocks = list(profiles.keys())
    profile_stock_quantities = list(profiles.values())
    return profile, profile_stocks, profile_stock_quantities

def addParticularStockAndQuantity(profile, stock, quantity):
    response = requests.put(BASE + "3000/profile/" + profile, json={"stock":stock, "quantity":quantity})

def removeParticularStock(profile, stock):
    response = requests.delete(BASE + "3000/profile/" + profile, json={"stock":stock})

def updateParticularQuantityOfStock(profile, stock, quantity):
    response = requests.put(BASE + "3000/profile/" + profile, json={"stock":stock, "quantity":quantity})

## Function for External API 
def getStocks(stockInput):            
    stock = yf.Ticker(stockInput)
    stockInfo = stock.info
    message_1 = stockInfo["longBusinessSummary"]
    message_2 = stockInfo["regularMarketPrice"]
    return message_1, message_2

"""

Integrated API Routes below

"""
# Web Service 1 
@app.route('/', methods=['GET', 'POST'])
def viewAccounts():
    account_names, account_statuses = AccountList()
    print(account_names)
    print(account_statuses)
    return render_template('accounts.html', title='View Accounts', account_names=account_names, account_statuses=account_statuses)

@app.route('/createAccount', methods=['GET', 'POST'])
def createAccount():
    form = CreateAccount()
    print('Adding account initiated')
    if request.method == 'POST':
        accountType = request.form.get('accountType')
        status = request.form.get('status')
        addAnAccount(accountType, status)
        return redirect(url_for('viewAccounts'))
    return render_template('createAccount.html', title='Create an Account', form=form)

@app.route('/removeAccount', methods=['GET', 'POST'])
def removeAccount():
    form = RemoveAccount()
    if request.method == 'POST':
        account = request.form.get('accountType')
        removeAnAccount(account)
        return redirect(url_for('viewAccounts'))
    return render_template('removeAccount.html', title='Remove an Account', form=form)

@app.route('/updateAccount', methods=['GET', 'POST'])
def updateAccount():
    form = UpdateAccount()  
    if request.method == 'POST':
        accountType = request.form.get('accountType')
        status = request.form.get('status')
        updateAnAccount(accountType, status)
        return redirect(url_for('viewAccounts'))
    return render_template('updateAccount.html', title='Update an Account', form=form)

@app.route('/viewDetails', methods=['GET', 'POST'])
def viewDetails():
    form = ViewDetails()
    if request.method == 'POST':
        account = request.form.get('accountType')
        return redirect(url_for('accountInfo', account=account))
    return render_template('viewDetails.html', title='View More Details on an Account', form=form)

## Redirect to Web Service 2
@app.route('/accountInfo', methods=['GET', 'POST'])
def accountInfo():
    account = request.args['account'] 
    try:
        profile, profile_stocks, profile_stock_quantities = getInfoForAccount(account)
    except ValueError as e:
        flash(Markup('Oops this there is no profile information about this account! Click <a href="/addStock" class="alert-link">here</a> to add a stock to this profile'))
        return redirect(url_for('viewDetails'))
    
    return render_template('accountInfo.html', title='View More Details on an Account', profile=profile, 
                            profile_stocks=profile_stocks, profile_stock_quantities=profile_stock_quantities)

@app.route('/addStock', methods=['GET', 'POST'])
def addStock():
    form = CreateStock()
    print('Adding stock initiated')
    if request.method == 'POST':
        profile = request.form.get('profile')
        stock = request.form.get('stock')
        quantity = request.form.get('quantity')
        print(profile, stock, quantity)
        addParticularStockAndQuantity(profile, stock, quantity)
        return redirect(url_for('accountInfo', account=profile))
    return render_template('addStock.html', title='Add a Stock', form=form)

@app.route('/removeStock', methods=['GET', 'POST'])
def removeStock():
    form = RemoveStock()
    if request.method == 'POST':
        profile = request.form.get('profile')
        stock = request.form.get('stock')
        removeParticularStock(profile, stock)
        return redirect(url_for('accountInfo', account=profile))
    return render_template('removeStock.html', title='Remove a Stock', form=form)

@app.route('/updateStock', methods=['GET', 'POST'])
def updateStock():
    form = UpdateStock()
    if request.method == 'POST':
        profile = request.form.get('profile')
        stock = request.form.get('stock')
        quantity = request.form.get('quantity')
        updateParticularQuantityOfStock(profile, stock, quantity)
        return redirect(url_for('accountInfo', account=profile))
    return render_template('updateStock.html', title='Update a Stock Quantity', form=form)

# Redirect to Web service 3 
## External API Client Integration
@app.route('/viewStockSummary', methods=['GET', 'POST'])
def viewStockSummary():
    message_1 = request.args['message_1'] 
    message_2 = request.args['message_2'] 
    return render_template('viewStockSummary.html', title='View Stock Summary', message_1=message_1, message_2=message_2)

## Redirects to get resource from External API
@app.route('/stockDetails', methods=['GET', 'POST'])
def stockDetails():
    form = Stock()
    if request.method == 'POST':
        stock = request.form.get('stock')
        message_1, message_2 = getStocks(stock)
        return redirect(url_for('viewStockSummary', message_1=message_1, message_2=message_2))
    return render_template('stockDetails.html', title='More about Stocks', form=form)


