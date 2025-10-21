from datetime import datetime

class Note:
    """ Represents a note with a title, content, and timestamp. """
    def __init__(self, note_id, title, content, timestamp=None):
        self.id = note_id
        self.title = title
        self.content = content
        self.timestamp = timestamp if timestamp else datetime.now()
        
class NoteModel:
    """ Model for managing notes. """
    def __init__(self):
        self.notes = {}
        self.next_id = 1
        
    def create(self, title, content):
        """ Create a new note. """
        note = Note(self.next_id, title, content)
        self.notes[self.next_id] = note
        self.next_id += 1
        return note
    
    def getall(self):
        """ Get all notes. """
        return list(self.notes.values())
    
    def getbyid(self, note_id):
        """ Get a note by its ID. """
        return self.notes.get(note_id)
    
    def search(self, keyword):
        """ Search notes by title or content. """
        results = [ note for note in self.notes.values()
                    if keyword.lower() in note.title.lower() or keyword.lower() in note.content.lower() ]
    
    def delete(self, note_id):
        return self.notes.pop(note_id, None)

class NoteModel:
    
    def __init__(self):
        self.notes = []

    def get_all_notes(self):
        return self.notes

    def add_note(self, note):
        self.notes.append(note)
