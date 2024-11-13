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
def render_page2():
    session["start_time"] = time.time()

    return render_template('question1.html')

@app.route('/startOver')
def startOver():
    session.clear() #clears variable values and creates a new session
    return redirect('/') # url_for('renderMain') could be replaced with '/'
@app.route("/answersOne",methods=['GET','POST'])
def page3():
    if "answer1" not in session:
        session["answer1"]=request.form['ques1']
    return render_template('question2.html')
@app.route("/answersTwo",methods=['GET','POST'])  
def page4():
    if "answer2" not in session:
        session["answer2"]=request.form['ques2']
    return render_template('question3.html')
@app.route("/answersThree",methods=['GET','POST'])
def page5():
    if "answer3" not in session:
        session["answer3"]=request.form['ques3']
    return render_template('question4.html')
@app.route("/answersFour",methods=['GET','POST'])
def page6():
    if "answer4" not in session:
        session["answer4"]=request.form['ques4']
    session["end_time"] = time.time()
    time_taken = session["end_time"] - session["start_time"]
    finalScore=get_score()
    return render_template('results.html', grade=finalScore, time_taken=time_taken)



def get_score():
    scoreVal=0
    if session["answer1"]=="256":
        scoreVal+=1
    if session["answer2"]=="2":
        scoreVal+=1
    if session["answer3"]=="20":
        scoreVal+=1
    if session["answer4"]=="612":
        scoreVal+=1
    return scoreVal
    
if __name__ == '__main__':
    app.run(debug=False)
