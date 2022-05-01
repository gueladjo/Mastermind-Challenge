from mastermindweb import app
from flask import Flask, session
from flask_session import Session
from flask import render_template, url_for, flash, redirect, request, Blueprint





gaming = Blueprint('game', __name__)
SESSION_TYPE = 'filesystem'
###Remove if causes bugs
app.config.from_object(__name__)

#To share data between requests, we can store data in a session instead of having to store in a database
#A session makes it possible to remember information from one request to another. The way Flask does this is by using a signed cookie
Session(app)



def resetdata():
    session['attempts'] = 0
    session['answer']= ""
    session['guesses'] = []

def initialize():
    if "answer" not in session:
        session["answer"]= ""
    if "attempts" not in session:
        session["attempts"]=0
    if 'guesses' not in session:
        session['guesses'] = []

