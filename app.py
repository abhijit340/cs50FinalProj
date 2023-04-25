from flask import Flask, flash, redirect, render_template, request, session
from helpers import login_req, 

app = Flask(__name__)

@app.route('/')
@login_req
def index():
    return "Hello World"

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/register', methods=["GET", "POST"])
def register():
        #get path sends user to registration screen
        if request.method == "GET":
            return render_template("register.html")    
        if request.method == "POST":
             #registion action begins here
             newUser = request.form.get("username")
             newPass = request.form.get("password")
             newPassCom = request.form.get("password_rep")


if __name__ == "__main__":
    app.run(debug=True)