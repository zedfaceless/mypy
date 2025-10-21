from flask import Flask
from controllers.note_controller import NoteController

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
    
    
    