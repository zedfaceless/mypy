# controllers/note_controller.py
from flask import render_template, request, redirect, url_for, session, flash
from models.note_model import NoteModel
from controllers.auth_controller import login_required

class NoteController:
    def __init__(self, app, notes_collection):
        self.app = app
        self.model = NoteModel(notes_collection)
        self.register_routes()

    def register_routes(self):
        self.app.add_url_rule("/dashboard", "dashboard", self.dashboard, methods=["GET"])
        self.app.add_url_rule("/notes", "notes_list", self.notes_list, methods=["GET"])
        self.app.add_url_rule("/notes/add", "notes_add", self.add_note, methods=["GET", "POST"])
        self.app.add_url_rule("/notes/<note_id>", "notes_detail", self.note_detail, methods=["GET"])
        self.app.add_url_rule("/notes/<note_id>/edit", "notes_edit", self.edit_note, methods=["GET", "POST"])
        self.app.add_url_rule("/notes/<note_id>/delete", "notes_delete", self.delete_note, methods=["POST"])

    @login_required
    def dashboard(self):
        # simple dashboard shows latest notes
        user_id = session["user_id"]
        notes = self.model.get_all_for_user(user_id)
        return render_template("dashboard.html", notes=notes)

    @login_required
    def notes_list(self):
        user_id = session["user_id"]
        q = request.args.get("q", "").strip()
        notes = self.model.search_for_user(user_id, q)
        return render_template("notes_list.html", notes=notes, q=q)

    @login_required
    def add_note(self):
        if request.method == "POST":
            title = request.form.get("title", "").strip()
            content = request.form.get("content", "").strip()
            if not title:
                flash("Title is required", "danger")
                return render_template("note_add.html", title=title, content=content)
            note = self.model.create(session["user_id"], title, content)
            flash("Note created", "success")
            return redirect(url_for("notes_list"))
        return render_template("note_add.html")

    @login_required
    def note_detail(self, note_id):
        note = self.model.get_by_id(note_id)
        if not note or note["user_id"] != session["user_id"]:
            flash("Note not found", "warning")
            return redirect(url_for("notes_list"))
        return render_template("note_detail.html", note=note)

    @login_required
    def edit_note(self, note_id):
        note = self.model.get_by_id(note_id)
        if not note or note["user_id"] != session["user_id"]:
            flash("Note not found", "warning")
            return redirect(url_for("notes_list"))
        if request.method == "POST":
            title = request.form.get("title", "").strip()
            content = request.form.get("content", "").strip()
            if not title:
                flash("Title required", "danger")
                return render_template("note_edit.html", note=note)
            updated = self.model.update(note_id, session["user_id"], title, content)
            if updated:
                flash("Note updated", "success")
                return redirect(url_for("notes_detail", note_id=note_id))
            flash("Update failed", "danger")
        return render_template("note_edit.html", note=note)

    @login_required
    def delete_note(self, note_id):
        success = self.model.delete(note_id, session["user_id"])
        if success:
            flash("Note deleted", "success")
        else:
            flash("Delete failed", "danger")
        return redirect(url_for("notes_list"))
