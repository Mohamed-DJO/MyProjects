# 📝 Flask TODO + Hobbies Tracker

This is a full-stack web app built using **Flask**, **SQLite**, and **Bootstrap** that allows users to:

- ✅ Register and log in securely
- 🧠 Track TODO tasks
- 🎯 Add personal hobbies
- 📂 Store data using SQLite + SQLAlchemy
- 💾 Use server-side sessions with Flask-Session

---

## 🚀 Features

- **Authentication**: Secure user registration and login with password hashing.
- **TODO Tracker**: Add tasks to your personal to-do list.
- **Hobby Tracker**: Add hobbies you're passionate about.
- **Session Management**: Persistent login with Flask-Session.
- **Database**: Models created using SQLAlchemy and stored in SQLite.
- **Responsive UI**: Styled with Bootstrap 5 and a custom CSS theme.

---

## 📂 Folder Structure

flask-todo-hobies/
│
├── app.py # Main Flask application
├── templates/ # HTML templates (Jinja2)
│ ├── layout.html
│ ├── login.html
│ ├── register.html
│ ├── todo.html
│ └── hobbie.html
├── static/ # CSS styling
│ └── styles.css
├── instance/ # SQLite DB (info.db)
├── requirements.txt # Python dependencies
└── .gitignore

🧠 Tech Stack
Python 3.x
Flask
Flask-Session
SQLAlchemy
SQLite
Bootstrap 5
