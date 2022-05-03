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
    session['startedgame'] = False

def initializesession():
    if "answer" not in session:
        session["answer"]= ""
    if "attempts" not in session:
        session["attempts"]=0
    if 'guesses' not in session:
        session['guesses'] = []
    if 'startedgame' not in session:
        session['startedgame'] = False
    

def calcultatescore():
    pass

def calculateposition():
    reds, whites = 0, 0
    if not session['answer'] or not session['guesses']: return (0, 0)

    answer, guess = session['answer'], session['guesses'][-1]
    if len(answer) != len(guess): return (0, 0)

    for key, digit in enumerate(guess):
        if digit == answer[key]:
            reds += 1
        else:
            for answerDigit in answer:
                if answerDigit == digit:
                    whites += 1
                    break   ###Only counting one number if guess equals 2 numbers in given combination

    return (reds, whites) if not None else (0,0)
                

