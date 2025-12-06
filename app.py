# app.py
from flask import Flask, redirect
from pymongo import MongoClient
from config import MONGO_URI, MONGO_DBNAME, SECRET_KEY

from controllers.auth_controller import AuthController
from controllers.note_controller import NoteController

def create_app():
    app = Flask(__name__, static_folder="static", template_folder="templates")
    app.config["SECRET_KEY"] = SECRET_KEY

    # MongoDB client
    client = MongoClient(MONGO_URI)
    db = client[MONGO_DBNAME]

    # Initialize controllers (they register routes on the app)
    AuthController(app, db["users"])
    NoteController(app, db["notes"])

    @app.route("/")
    def root():
        return redirect("/dashboard")

    return app

# Gunicorn WSGI entrypoint
application = create_app()

if __name__ == "__main__":
    application.run(debug=True)
