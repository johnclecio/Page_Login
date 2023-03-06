from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/index.html')
def index():
    return render_template('/index.html')


@app.route('/login.html')
def login():
    return render_template('/login.html')


@app.route('/check_login', methods=['POST',])
def check_login():
    user = request.form['email']
    password = request.form['password']
    if user == "admin@admin.com" and password == "admin123":
        return redirect('/main_page')
    else:
        return redirect('/login.html')


@app.route('/cadastrar.html')
def cadastrar():
    return render_template('/cadastrar.html')


@app.route('/main_page')
def main_page():
    return "<h1>LOG</h1>"


app.run(debug=True)
