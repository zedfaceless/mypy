# controllers/auth_controller.py
from flask import render_template, request, redirect, url_for, session, flash
from models.user_model import UserModel

def login_required(f):
    from functools import wraps
    @wraps(f)
    def wrapped(*args, **kwargs):
        if "user_id" not in session:
            return redirect(url_for("login"))
        return f(*args, **kwargs)
    return wrapped

class AuthController:
    def __init__(self, app, users_collection):
        self.app = app
        self.user_model = UserModel(users_collection)
        self.register_routes()

    def register_routes(self):
        self.app.add_url_rule("/register", "register", self.register, methods=["GET", "POST"])
        self.app.add_url_rule("/login", "login", self.login, methods=["GET", "POST"])
        self.app.add_url_rule("/logout", "logout", self.logout, methods=["GET"])

    def register(self):
        if request.method == "POST":
            username = request.form.get("username", "").strip()
            password = request.form.get("password", "")
            if not username or not password:
                flash("Username and password are required", "danger")
                return render_template("register.html", username=username)
            if self.user_model.find_by_username(username):
                flash("Username already exists", "warning")
                return render_template("register.html", username=username)
            user_id = self.user_model.create_user(username, password)
            session["user_id"] = user_id
            session["username"] = username
            flash("Registration successful", "success")
            return redirect(url_for("dashboard"))
        return render_template("register.html")

    def login(self):
        if request.method == "POST":
            username = request.form.get("username", "").strip()
            password = request.form.get("password", "")
            if self.user_model.verify_password(username, password):
                user = self.user_model.find_by_username(username)
                session["user_id"] = str(user["_id"])
                session["username"] = user["username"]
                flash("Logged in", "success")
                return redirect(url_for("dashboard"))
            flash("Invalid credentials", "danger")
            return render_template("login.html", username=username)
        return render_template("login.html")

    def logout(self):
        session.clear()
        flash("Logged out", "info")
        return redirect(url_for("login"))
