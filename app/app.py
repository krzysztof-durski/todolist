from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)   
app.config.from_object('app.config')

tasks=[]

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    title = request.form.get('title')
    description = request.form.get('description')
    if title:
        tasks.append({'title': title, 'description': description, 'completed': False})
    return redirect('/')

@app.route('/update/<int:task_id>', methods=['UPDATE'])
def update_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks[task_id]['completed'] = not tasks[task_id]['completed']
    return redirect('/')

@app.route('/delete/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
    return redirect('/')