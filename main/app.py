# Web APP Dependencies
from flask import Flask, render_template, request, session, redirect, flash

#DB Dependencies
import sqlite3 as sql

#graph stuff
import matplotlib



#For testing

app = Flask(__name__)

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route('/')
def index():
    return render_template('index.html', login = loginstate[m_login_state])


@app.route('/contact', methods=["GET","POST"])
def contact():
    return render_template('contact.html', login = loginstate[m_login_state])

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)