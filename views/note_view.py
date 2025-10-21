from flask import jsonify

class NoteView:
    
    def to_dict(self, note):
        """ Format reponses for note resources """
        return {
            'id': note.id,
            'title': note.title,
            'content': note.content,
            'timestamp': note.timestamp.isoformat()
        }
    
    def render_list(self, notes):
        """ Render a list of notes """
        return jsonify([self.to_dict(note) for note in notes])
    
    def render_one(self, note):
        """ Render a one note """
        if note:
            return jsonify(self.to_dict(note))
        return jsonify({'message': 'Note not found'}), 404
    
    def render_message(self, message, status=200):
        """ Render a message response """
        return jsonify({'message': message}), status