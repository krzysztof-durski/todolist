from flask import Flask, redirect, request, url_for, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)   
app.config.from_object('app.config')

db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    completed = db.Column(db.Boolean, default=False)

with app.app_context():
    db.create_all()
    
tasks = []

@app.route('/')
def index():
    tasks = Task.query.all()  
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    title = request.form.get('title')
    description = request.form.get('description')
    if title:
        new_task = Task(title=title, description=description)
        db.session.add(new_task)  
        db.session.commit()       
    return redirect('/')

@app.route('/update/<int:task_id>', methods=['POST'])
def update_task(task_id):
    task = Task.query.get(task_id)  
    if task:
        task.completed = not task.completed
        db.session.commit()  
    return redirect('/')

@app.route('/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    task = Task.query.get(task_id)  
    if task:
        db.session.delete(task)  
        db.session.commit()      
    return redirect('/')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/legal')
def legal():
    return render_template('legal.html')