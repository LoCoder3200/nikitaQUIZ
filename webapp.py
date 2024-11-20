from flask import Flask, request, render_template, flash
from markupsafe import Markup
from flask import redirect
from flask import session
import os
import time

app = Flask(__name__)
app.secret_key=os.environ["SECRET_KEY"]; #This is an environment variable.  

@app.route("/")
def render_main():
    return render_template('index.html')
@app.route("/page2")
def render_pageTwo():
    return render_template('page2.html')
@app.route("/question2",methods=['GET','POST'])
def render_pageThree():
    if "answer1" not in session:
        session["answer1"]=request.form['questionONE']
    return render_template('page3.html')
@app.route("/question3",methods=['GET','POST'])
def render_pageFour():
    if "answer2" not in session:
        session["answer2"]=request.form['questionTWO']
    return render_template('page4.html')
@app.route('/startOver')
def startOver():
    session.clear() #clears variable values and creates a new session
    return redirect('/') # url_for('renderMain') could be replaced with '/'

    
if __name__ == '__main__':
    app.run(debug=False)
