# models/note_model.py
from bson import ObjectId
from datetime import datetime

def _serialize(doc):
    if not doc:
        return None
    d = dict(doc)
    d["_id"] = str(d["_id"])
    if "created_at" in d and isinstance(d["created_at"], datetime):
        d["created_at"] = d["created_at"].isoformat()
    return d

class NoteModel:
    def __init__(self, collection):
        self.collection = collection

    def create(self, user_id, title, content):
        doc = {
            "user_id": user_id,
            "title": title,
            "content": content,
            "created_at": datetime.utcnow(),
            "updated_at": datetime.utcnow()
        }
        res = self.collection.insert_one(doc)
        return self.get_by_id(str(res.inserted_id))

    def get_all_for_user(self, user_id):
        cursor = self.collection.find({"user_id": user_id}).sort("created_at", -1)
        return [_serialize(d) for d in cursor]

    def get_by_id(self, note_id):
        try:
            doc = self.collection.find_one({"_id": ObjectId(note_id)})
            return _serialize(doc)
        except Exception:
            return None

    def update(self, note_id, user_id, title, content):
        try:
            res = self.collection.update_one(
                {"_id": ObjectId(note_id), "user_id": user_id},
                {"$set": {"title": title, "content": content, "updated_at": datetime.utcnow()}}
            )
            if res.matched_count:
                return self.get_by_id(note_id)
            return None
        except Exception:
            return None

    def delete(self, note_id, user_id):
        try:
            res = self.collection.delete_one({"_id": ObjectId(note_id), "user_id": user_id})
            return res.deleted_count > 0
        except Exception:
            return False

    def search_for_user(self, user_id, keyword):
        if not keyword:
            return self.get_all_for_user(user_id)
        cursor = self.collection.find({
            "user_id": user_id,
            "$or": [
                {"title": {"$regex": keyword, "$options": "i"}},
                {"content": {"$regex": keyword, "$options": "i"}}
            ]
        }).sort("created_at", -1)
        return [_serialize(d) for d in cursor]
