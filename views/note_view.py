# views/note_view.py
from flask import render_template, jsonify

class NoteView:
    def render_list(self, notes):
        return render_template("notes_list.html", notes=notes)

    def render_one(self, note):
        return render_template("note_detail.html", note=note)

    def render_message(self, message, status=200):
        return jsonify({"message": message}), status
