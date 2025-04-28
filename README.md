# todolist :)

## Is deployed at:

https://todolist-emix.onrender.com

## What is that?

It is a simple TO-DO APP, lightweight web-based task management application. It allows users to create, update, delete, and mark tasks as completed.

## Requirements

- All the requirements are in: requirements.txt
- Install by: pip install -r requirements.txt

### Technology used:

- Backend:
  - Flask: A lightweight web framework.
  - Flask-SQLAlchemy: ORM for database management.
  - Gunicorn: A production-ready WSGI server.
- Frontend:
  - HTML5 and CSS3 for basic UI.
  - Jinja2 templating engine for dynamic content rendering.
- Database:
  - PostgreSQL
- Environment Management:
  - python-dotenv: For loading environment variables.
- ChatGPT for creating README file.

## Installation

1. Clone the repository:
   git clone [<repository_url>](https://github.com/krzysztof-durski/todolist.git)
   cd todo-app

2. Create and activate a virtual environment:

   python -m venv venv

   source venv/bin/activate

3. Install the dependencies:

   pip install -r requirements.txt

4. Set up the database:

   python -c "from app.app import db; db.create_all()"

5. Run the app:

   python run.py

6. Open your browser and visit:

   http://127.0.0.1:5000
