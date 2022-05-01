from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from mastermindweb.game.gaming import initialize, resetdata
from mastermindweb.game.forms import GuessingForm
from flask_restful import abort
from mastermindweb import db
from mastermindweb import app
from flask import Flask, session
import random

game = Blueprint('game', __name__)
##########Store guesses in set#########


@game.route('/dificulty', methods=['GET', 'POST'])
def chooselevel():
    
    return render_template('game_pages/levelpage.html')


@game.route('/startgame/mastermind', methods=['GET', 'POST'])
def startgame():
    ###########Adding values to keys to prevent key errors###########
    initialize()

      
    form = GuessingForm()
    guess = str(form.guesscombo.data)
    session['guesses'].append(guess)
    print(f"Previous guesses are {session['guesses']}")




    print((guess, session['answer'] if session['answer'] else ""))
    
    if (guess and session['answer']) and guess == session['answer']: 
        print(f"You have found the correct positions in {session['attempts']} attempt(s)")
        resetdata()
        flash('You have found the answer')

    
    if session['attempts'] == 0:
        answercode = ""
        for i in range(4):
            answercode += str(random.randint(0, 9))
        session["answer"] = answercode
    
    session['attempts'] += 1 if guess else 0
    
    return render_template('game_pages/gamepage.html', form=form, answer=session['answer'], attempts=session['attempts'])





    









