from flask import Flask, request#importing request will allow us to see what data was sent through api side
from flask_restful import Api, Resource, reqparse

app =  Flask(__name__)
api = Api(app)

profile_put_args = reqparse.RequestParser()
profile_put_args.add_argument("stock", type=str, help="Name of stock is required", required=True)
profile_put_args.add_argument("quantity", type=int, help="Quantity of stock owned is required", required=True)

profile_delete_args = reqparse.RequestParser()
profile_delete_args.add_argument("stock", type=str, help="Name of stock is required", required=True)

profiles={"Current":{"Meta":5, "Google":3, "Amazon":7},
        "Savings":{"Meta":3, "Google":1, "Amazon":9},
        "Business":{"Meta":5, "Google":3}}

#making a resource
class profile(Resource):#inherits from Resource
    def get(self, profile_id):
        return profiles[profile_id]

    def put(self, profile_id):
        args = profile_put_args.parse_args()
        #need only the values of the args which is dict type because of how I defined profiles
        pairOfValues = list(args.values())
        profiles[profile_id][pairOfValues[0]] = pairOfValues[1]
        return profiles[profile_id]

    def delete(self,profile_id):
        arg = profile_delete_args.parse_args()
        value = list(arg.values())
        del profiles[profile_id][value[0]]
        return (value[0]+ " stock removed")

    def update(self,profile_id):
        args = profile_put_args.parse_args()
        pairOfValues = list(args.values())
        profiles[profile_id][pairOfValues[0]] = pairOfValues[1]
        return (pairOfValues[0]+ "updated")


#register the resource above

api.add_resource(profile, "/profile/<string:profile_id>")


if __name__ == "__main__":
    app.run(debug=True, port=3000)


