import os
from flask import Flask, render_template, request
import psycopg2

ALLOWED_EXTENSIONS = ['']
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads/'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.secret_key = "therearenoneinexistance"
DB_HOST = "Yes"
DB_NAME = "name"
DB_USER = "user"
DB_PASS = "password"
# conn = psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port="5432")
#cursor = conn.cursor()


@app.route("/")
def hello():
    name = request.args.get("name", "Flask")
    return f"Hello, {name}!"

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/login")
def login():
    return render_template("login.html")

if __name__ == '__main__':
    app.run(debug=True)
