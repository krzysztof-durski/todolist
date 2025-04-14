from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)   

app.config.from_object('app.config')

@app.route('/')
def index():
    return render_template('index.html')