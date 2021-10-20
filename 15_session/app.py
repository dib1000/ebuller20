# Team Snaps (Emma Buller, Theo Fahey, Angela Zhang)
# SoftDev
# K14 -- Form and Function (Flask and Forms)
# 2021-10-14

from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission
from flask import session
import os

#the conventional way:
#from flask import Flask, render_template, request

app = Flask(__name__)    #create Flask object
app.secret_key = os.urandom(32)


'''
trioTASK:
~~~~~~~~~~~ BEFORE RUNNING THIS, ~~~~~~~~~~~~~~~~~~
...read for understanding all of the code below.
Some will work as written; other sections will not. Can you predict which?
Devise some simple tests you can run to "take apart this engine," as it were.
Execute your tests. Process results.
PROTIP: Insert your own in-line comments wherever they will help your future self and/or current teammates understand what is going on.
'''

@app.route("/") #, methods=['GET', 'POST'])
def disp_loginpage():
    print(session)
    if session.get("name"):
        return loggedIn()
    # print("\n\n\n")
    # print("***DIAG: this Flask obj ***")
    # print(app) #prints app
    # print("***DIAG: request obj ***")
    # print(request) #prints link and methods
    # print("***DIAG: request.args ***")
    # print(request.args) #prints empty dictionary since there have been no arguments inputted
    # #print("***DIAG: request.args['username']  ***") <- only works after submitting form
    # #print(request.args['username'])
    # print("***DIAG: request.headers ***")
    # print(request.headers)  #prints various information
    return render_template( 'login.html', error = '' ) #webpage is just the login.html file in templates


@app.route("/auth") # , methods=['GET', 'POST'])
def authenticate():
    if (request.args['username'] != "Snaps") or (request.args['password'] != "snaps123"):
        return Error('response.html', username = session["name"])
    #print("\n\n\n")
    #print("***DIAG: this Flask obj ***")
    #print(app) #same thing as disp_loginpage()
    #print("***DIAG: request obj ***")
    #print(request) #link of page (with the inputs from the form)
    #print("***DIAG: request.args ***")
    #print(request.args) #not empty anymore
    #print("***DIAG: request.args['username']  ***")
    #print(request.args['username']) #prints the username that you inputted
    #print("***DIAG: request.headers ***")
    #print(request.headers) #same as disp_loginpage
    m = request.method #either get or post
    if len(session) == 0:
        session["name"] = request.args['username']
        session["password"] = request.args['password']
    #print(request.form['username'])
    return render_template('response.html', username = session["name"], method = m)

@app.route("/out")
def out():
    #print(len(session))
    if len(session) > 0:
        session.pop("name")
        session.pop("password")
    #print(len(session))
    return render_template('login.html', error = '')

@app.route("/empty")
def Error():
    message = "BAD! Login again "
    return render_template('login.html', error = message)

@app.route("/in")
def loggedIn():
    return render_template('response.html', username = session["name"], method = "GET")

if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()
