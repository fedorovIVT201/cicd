from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index_page():
   message = 'Добро пожаловать!, 2'
   return render_template('index.html', message=message)