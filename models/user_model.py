# models/user_model.py
from bson import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash

class UserModel:
    def __init__(self, collection):
        self.collection = collection

    def create_user(self, username, password):
        # store hashed password
        hashpw = generate_password_hash(password)
        res = self.collection.insert_one({
            "username": username,
            "password": hashpw,
            "created_at": None
        })
        return str(res.inserted_id)

    def find_by_username(self, username):
        return self.collection.find_one({"username": username})

    def find_by_id(self, user_id):
        try:
            doc = self.collection.find_one({"_id": ObjectId(user_id)})
            if not doc:
                return None
            doc["_id"] = str(doc["_id"])
            return doc
        except Exception:
            return None

    def verify_password(self, username, password):
        user = self.find_by_username(username)
        if not user:
            return False
        return check_password_hash(user["password"], password)
