from datetime import datetime
from bson.objectid import ObjectId

class Note:
    """Represents a note with a title, content, and timestamp."""
    def __init__(self, note_id, title, content, timestamp=None):
        self.id = note_id
        self.title = title
        self.content = content
        self.timestamp = timestamp if timestamp else datetime.now()


class NoteModel:
    def __init__(self, collection):
        self.collection = collection

    def get_all(self):
        return list(self.collection.find())

    def get_by_id(self, note_id):
        return self.collection.find_one({"_id": ObjectId(note_id)})

    def create(self, title, content):
        result = self.collection.insert_one({"title": title, "content": content})
        return self.get_by_id(result.inserted_id)

    def delete(self, note_id):
        result = self.collection.delete_one({"_id": ObjectId(note_id)})
        return result.deleted_count > 0

    def search(self, keyword):
        results = list(self.collection.find({
            "$or": [
                {"title": {"$regex": keyword, "$options": "i"}},
                {"content": {"$regex": keyword, "$options": "i"}}
            ]
        }))
        return results