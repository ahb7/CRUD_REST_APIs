from flask import Flask, Response, request, jsonify 
from pymongo import MongoClient
import json
from bson.objectid import ObjectId 

app = Flask(__name__)

try:  
    client = MongoClient('localhost', 27017)
except Exception as ex:
    print(ex)
    print("Failed to connect to the MongoDB")

# MongoDb database
db = client.corider_database

# Users collection
users = db.users

# Create User
@app.route("/users", methods=["POST"])
def create_user():
    try:
        user = {
            "name": request.form["name"],
            "email": request.form["email"],
            "password": request.form["password"]
        }
        dbResponse = users.insert_one(user)
        print(dbResponse.inserted_id)
        return Response(
            response = json.dumps(
                {"message":"User created",
                "id":f"{dbResponse.inserted_id}"
                }
            ),
            status=200,
            mimetype="application/json"
        )
    except Exception as ex:
        print(ex)
        return Response(
            response = json.dumps({"message":"Can not create user"}),
            status=500,
            mimetype="application/json"
        )

# Read All Users
@app.route("/users", methods=["GET"])
def read_users():
    try:
        data = list(users.find())
        for user in data:
            user["_id"] = str(user["_id"])
        return Response(
            response = json.dumps(data),
            status=200,
            mimetype="application/json"
        )
    except Exception as ex:
        print(ex)
        return Response(
            response = json.dumps({"message":"Can not read users"}),
            status=500,
            mimetype="application/json"
        )

# Read an User
@app.route("/users/<id>", methods=["GET"])
def read_an_user(id):
    try:
        data = users.find_one({"_id":ObjectId(id)})
        return Response(
            response = json.dumps(data, default=str),
            status=200,
            mimetype="application/json"
        )
    except Exception as ex:
        print(ex)
        return Response(
            response = json.dumps({"message":"Can not read the user"}),
            status=500,
            mimetype="application/json"
        )

# Update User
@app.route("/users/<id>", methods=["PUT"])
def update_user(id):
    try:
        dbResponse = users.update_one(
            {"_id":ObjectId(id)},
            {"$set":{"name":request.form["name"], 
                     "email":request.form["email"],
                     "password":request.form["password"]}
            }      
        )
        return Response(
            response = json.dumps({"message":"User updated"}),
            status=200,
            mimetype="application/json"
        )
    except Exception as ex:
        print(ex)
        return Response(
            response = json.dumps({"message":"Can not update user"}),
            status=500,
            mimetype="application/json"
        )

# Delete User
@app.route("/users/<id>", methods=["DELETE"])
def delete_user(id):
    try:
        dbResponse = users.delete_one({"_id":ObjectId(id)})
        if dbResponse.deleted_count == 1:
            return Response(
                response = json.dumps({"message":"User deleted", "id":f"{id}"}),
                status=200,
                mimetype="application/json"
            )
        else:
            return Response(
                response = json.dumps({"message":"User not found", "id":f"{id}"}),
                status=200,
                mimetype="application/json"
            )
    except Exception as ex:
        print(ex)
        return Response(
            response = json.dumps({"message":"Can not delete user"}),
            status=500,
            mimetype="application/json"
        )

if __name__ == "__main__":
    app.run(debug=True)
