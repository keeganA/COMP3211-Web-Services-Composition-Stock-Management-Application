# Created by Shruti Naik sc20srn on 14/11/2022
# Flask-RESTful documentation used for implementation (linked below)
# https://flask-restful.readthedocs.io/en/latest/quickstart.html#full-example

from flask import Flask, jsonify, request
from flask_restful import abort, Api, Resource, reqparse

app = Flask(__name__)
app.config['BUNDLE_ERRORS'] = True
api = Api(app)

accounts = { 'ChildrensFund': 'Closed',
             'Business': 'Open',
             'Current': 'Open',
             'Student': 'Closed',
             'Credit': 'Open' }

# Parsers to add an account
account_parser = reqparse.RequestParser()
account_parser.add_argument('Account', type=str, help="Account Name is required", required=True)
account_parser.add_argument('Status', type=str, help="Status of Account is required", required=True)

# Create an Account
class Account(Resource):
    def get(self, accountType):
        # Abort execution if an invalid account name is entered
        if accountType not in accounts:
            abort(404, message="Cannot find Account {}".format(accountType))
        return jsonify(accountType, accounts[accountType])

    def post(self, accountType):
        args = account_parser.parse_args()
        values = list(args.values())
        # Abort execution if an account name that already exists is entered
        if accountType in accounts:
            abort(404, message="Account {} already exists".format(accountType))
        accounts[accountType] = values[1]
        return 'Account Successfully Added!', 201
    
    def delete(self, accountType):
        # Abort execution if an account name that doesn't exist is entered
        if accountType not in accounts:
            abort(404, message="Cannot find Account {}".format(accountType))
        del accounts[accountType]
        return 'Account successfully deleted', 204

    def update(self, accountType):
        args = account_parser.parse_args()
        values = list(args.values())
        # Abort execution if an account name that doesn't exist is entered
        if accountType not in accounts:
            abort(404, message="Cannot find Account {}".format(accountType))
        accounts[accountType] = values[1]
        return 'Account Successfully Updated!', 201

# View all Accounts
class Accounts(Resource):
    def get(self):
        return accounts

# Register resources
api.add_resource(Accounts, '/accounts', )
api.add_resource(Account, '/accounts/<accountType>', endpoint='Account')

if __name__ == "__main__":
	app.run(debug=True)