# 📝 Flask MVC Notes App

A simple **Notes Management Web Application** built with **Python** and **Flask**, designed to demonstrate the **MVC (Model-View-Controller)** architecture, **RESTful API principles**, and **Object-Oriented Programming (OOP)** concepts.

---

## Features

- Add, view, and list notes dynamically
- Uses **MVC pattern** for clean separation of logic
- RESTful routes for scalable web design
- Built with **Object-Oriented Programming** principles
- Lightweight and beginner-friendly project
- Data stored in memory (can easily extend to database later)

---

## Project Structure

```
mypy/
│
├── app.py                     # Main Flask application
│
├── controllers/               # Handles app logic and routes
│   └── note_controller.py
│
├── models/                    # Defines the data model and logic
│   └── note_model.py
│
├── views/                     # Jinja2 templates (HTML files)
│   ├── index.html
│   ├── notes.html
│   └── add_note.html
│
└── README.md
```

---

## Understanding the Design

### Model-View-Controller (MVC)

- **Model** → Manages data (NoteModel)
- **View** → User interface (HTML templates)
- **Controller** → Connects Model and View (NoteController)

### ⚙️ REST Architecture

Each route follows REST conventions:
| Method | Endpoint | Description |
|--------|----------------|----------------------|
| GET | `/notes` | Get all notes |
| GET | `/notes/add` | Render add note page |
| POST | `/notes/add` | Add a new note |

### Object-Oriented Approach

The project uses classes like `NoteModel` and `NoteController` to keep code modular, reusable, and easier to maintain.

---

## Installation & Running

### 1️ Clone the repository

```bash
git clone https://github.com/zedfaceless/mypy.git
cd mypy
```

### 2️ Install dependencies

```bash
pip install flask
```

### 3️ Run the app

```bash
python app.py
```

Then open your browser and go to [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## Technologies Used

- **Python 3**
- **Flask**
- **Jinja2 Templates**
- **MVC Architecture**
- **RESTful Routing**
- **Object-Oriented Programming (OOP)**

---

## 👨‍💻 Author

**Melchizedek Fernandez**  
Santa Cruz, Zambales, Philippines  
[zedfaces.fernandez@gmail.com](mailto:zedfaces.fernandez@gmail.com)  
[LinkedIn](https://www.linkedin.com/in/melchizedek-fernandez/) | [GitHub](https://github.com/zedfaceless)

---

## Future Improvements

- Integrate a database (SQLite or PostgreSQL)
- Add authentication (login & registration)
- Build a front-end with React or Vue
- Deploy online using Render or Railway

---

## Learning Goals

This project is part of my personal study on:

- Building modular Flask applications
- Applying MVC and REST principles
- Practicing object-oriented Python
- Preparing for backend development roles

---

✨ _“Clean code is simple, direct, and elegant — just like this app.”_ ✨
