from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from flask_restful import abort
from mastermindweb import db
from mastermindweb import app
from mastermindweb.game.forms import GuessingForm
from flask import Flask, session
from flask_session import Session
import random

SESSION_TYPE = 'filesystem'
###Remove if causes bugs
app.config.from_object(__name__)

#To share data between requests, we can store data in a session instead of having to store in a database
#A session makes it possible to remember information from one request to another. The way Flask does this is by using a signed cookie
Session(app)

game = Blueprint('game', __name__)
##########Store guesses in set#########
guess_seen = set()


@game.route('/dificulty', methods=['GET', 'POST'])
def chooselevel():
    
    return render_template('game_pages/levelpage.html')


@game.route('/startgame/mastermind', methods=['GET', 'POST'])
def startgame():
    if "counter" not in session:
        session["counter"]=[]
    if "attempts" not in session:
        session["attempts"]=0

      

    answer = ""
    form = GuessingForm()
    guess = str(form.guesscombo.data)
    guess_seen.add(guess)

    print((guess, session['counter'][-1] if session['counter'] else 0))
    
    if (guess and session['counter']) and guess == session['counter'][-1]: 
        print("You have found the correct positions")
        session['attempts'] = 0
        session['counter']= [] 
        flash('You have found the answer')

    
    for i in range(4):
        
        answer += str(random.randint(0, 8))
    session["counter"].append(answer)
    
    session['attempts'] += 1
    print(session['counter'])
    #session['attempts'] = 0
    #session['counter']= []
    return render_template('game_pages/gamepage.html', form=form, answer=answer, attempts=session['attempts'])








