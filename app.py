from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)   

app.config.from_object('config')
url_for('static', filename='css/main.css')

@app.route('/')
def index():
    return render_template('index.html')










if __name__ == '__main__':
    app.run()