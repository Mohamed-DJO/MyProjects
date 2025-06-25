from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from flask_sqlalchemy import SQLAlchemy
from functools import wraps

# Configure Flask app
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///info.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# ----------------------
# Models
# ----------------------
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    todo = db.Column(db.String(200), nullable=False)

class Hobby(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    hobby = db.Column(db.String(200), nullable=False)

# ----------------------
# Helpers
# ----------------------
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function

# ----------------------
# Routes
# ----------------------
@app.route("/")
@login_required
def index():
    return redirect("/todo")

@app.route("/login", methods=["GET", "POST"])
def login():
    session.clear()

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if not username or not password:
            return redirect("/")

        user = User.query.filter_by(username=username).first()
        if not user or not check_password_hash(user.password, password):
            return redirect("/")

        session["user_id"] = user.id
        return redirect("/")

    return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():
    session.clear()

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        if not username or not password or not confirmation:
            return redirect("/")

        if password != confirmation:
            return redirect("/")

        if User.query.filter_by(username=username).first():
            return redirect("/")

        hashed_password = generate_password_hash(password)
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        session["user_id"] = new_user.id
        return redirect("/")

    return render_template("register.html")

@app.route("/todo", methods=["GET", "POST"])
@login_required
def todo():
    if request.method == "POST":
        task = request.form.get("todo")
        if task:
            new_todo = Todo(user_id=session["user_id"], todo=task)
            db.session.add(new_todo)
            db.session.commit()
        return redirect("/todo")
    else:
        todos = Todo.query.filter_by(user_id=session["user_id"]).all()
        return render_template("todo.html", todos=todos)

@app.route("/hobbies", methods=["GET", "POST"])
@login_required
def hobbies():
    if request.method == "POST":
        hobby = request.form.get("hobbie")  # keep this name if your form uses "hobbie"
        if hobby:
            new_hobby = Hobby(user_id=session["user_id"], hobby=hobby)
            db.session.add(new_hobby)
            db.session.commit()
        return redirect("/hobbies")
    else:
        hobbies = Hobby.query.filter_by(user_id=session["user_id"]).all()
        return render_template("hobbie.html", hobbies=hobbies)

# ----------------------
# Run App
# ----------------------
if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Creates tables if they don't exist
    app.run(debug=True)
