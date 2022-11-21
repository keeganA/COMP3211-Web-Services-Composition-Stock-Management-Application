from  flask_wtf import Form 
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired
import requests, json

BASE = "http://127.0.0.1:"

class CreateAccount(Form):
    accountType = StringField('accountType', validators=[DataRequired()])
    status = StringField('status', validators=[DataRequired()])

class RemoveAccount(Form):
    accountType = StringField('accountType', validators=[DataRequired()])

class UpdateAccount(Form):
    accountType = StringField('accountType', validators=[DataRequired()])
    status = StringField('status', validators=[DataRequired()])

class ViewDetails(Form):
    accountType = StringField('accountType', validators=[DataRequired()])

class CreateStock(Form):
    profile = StringField('profile', validators=[DataRequired()])
    stock = StringField('stock', validators=[DataRequired()])
    quantity = StringField('quantity', validators=[DataRequired()])

class RemoveStock(Form):
    profile = StringField('profile', validators=[DataRequired()])
    stock = StringField('stock', validators=[DataRequired()])

class UpdateStock(Form):
    profile = StringField('profile', validators=[DataRequired()])
    stock = StringField('stock', validators=[DataRequired()])
    quantity = StringField('quantity', validators=[DataRequired()])

class Stock(Form):
    stocks = ['AAPL','BAC','AMZN','T','GOOG','MO','DAL','AA','AXP','DD','BABA','AIG','ALL','ADBE','GOOGL','ACN',
    'MT','LLY','APA','NLY','ADSK','ADM','AX','WBA','APD','AMBA','NVS',
    'CS','AMTD','ARCC','UBS','ARLP','ATO']
    stock = SelectField('stock', choices = stocks, validators=[DataRequired()])