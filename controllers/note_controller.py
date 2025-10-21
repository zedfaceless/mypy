from flask import request, redirect, render_template
from models.note_model import NoteModel
from views.note_view import NoteView

class NoteController:
    """ Connecting routes to model and views logic """
    
    def __init__(self, app):
        self.app = app
        self.model = NoteModel()
        self.view = NoteView()
        self.register_routes()
    
    def register_routes(self):
        """Register REST endpoints."""
        self.app.add_url_rule('/notes/add', 'add_note', self.add_note, methods=['GET', 'POST'])
        self.app.add_url_rule('/', 'home', self.home, methods=['GET'])
        self.app.add_url_rule("/notes", view_func=self.get_notes, methods=["GET"])
        self.app.add_url_rule("/notes/<int:note_id>", view_func=self.get_note, methods=["GET"])
        self.app.add_url_rule("/notes", view_func=self.create_note, methods=["POST"])
        self.app.add_url_rule("/notes/<int:note_id>", view_func=self.delete_note, methods=["DELETE"])
    
    def home(self):
        return "Welcome to your Notes App! Use /notes to view all notes."
    
    def add_note(self):
        if request.method == 'POST':
            title = request.form.get('title')
            content = request.form.get('content')
            new_note = {'title': title, 'content': content}
            self.model.add_note(new_note)
            return redirect('/notes')
        else:
            return render_template('add_note.html')

    # THE METHOD OF CONTROLLER TO GET ALL NOTES #
    
    def get_notes(self):
        keyword = request.args.get('search')
        if keyword:
            notes = self.model.search(keyword)
        else:
            notes = self.model.getall()
        return self.view.render_list(notes)
    
    def get_note(self, note_id):
        note = self.model.getbyid(note_id)
        return self.view.render_one(note)
    
    def create_note(self):
        data = request.get_json()
        title = data.get('title')
        content = data.get('content', '')
        if not title or not content:
            return self.view.render_message('Title and content are required', status=400)
        note = self.model.create(title, content)
        return self.view.render_one(note)
    
    def delete_note(self, note_id):
        deleted = self.model.delete(note_id)
        if deleted:
            return self.view.render_message(f'Note {note_id}deleted successfully')
        return self.view.render_message('Note not found', status=404)
    
    