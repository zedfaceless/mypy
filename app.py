
from flask import Flask
from controllers.note_controller import NoteController
from pymongo import MongoClient
from config import MONGO_URI

client = MongoClient(MONGO_URI)
db = client.get_default_database()    # points to 'mypy' database
notes_collection = db["note_user"]   # points to your collection

class App:
    """ Main application class to initialize Flask app and controllers + MVC structure """
    
    def __init__(self):
        self.app = Flask(__name__)
        self.note_controller = NoteController(self.app)
        
    def note_controller(self):
        NoteController(self.app)
    
    def run(self):
        self.app.run(debug=True)
    
if __name__ == '__main__':
    application = App()
    application.run()
    
    
    