from tracemalloc import start
from turtle import position
from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from mastermindweb.game.gaming import initializesession, resetdata, calcultatescore, calculateposition
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
    initializesession()
    startedgame = False
    ####Save user input into guess variable#####
    form = GuessingForm()
    validated = form.validate_on_submit() or form.validate_guess(form.guesscombo)


    print(f"These are the forms {validated}")
    if validated == None or validated == False: 
        flash('Please enter a valid number combination!') 
        return render_template('game_pages/gamepage.html', form=form, answer=session['answer'], attempts=max(1,session['attempts']), 
                            correctposition=0, wrongposition=0)


    guess = str(form.guesscombo.data)
    if guess != 'None' or not validated: session['guesses'].append(guess)
    print(f"Previous guesses are {session['guesses']}")

    positions = calculateposition()
    correctpositiondigits = positions[0] if positions else 0
    wrongpositiondigits = positions[1] if positions else 0


    print((guess, session['answer'] if session['answer'] else ""))
    #######If we've found the answer##########################
    if (guess and session['answer']) and guess == session['answer']: 
        print(f"You have found the correct positions in {session['attempts']} attempt(s)")
        score = calcultatescore()#####To implement later, we will also add to database in order to create leaderboard
        resetdata()
        positions = (0, 0)
        return render_template('game_pages/gamepage.html', form=form, answer=session['answer'], attempts=max(1,session['attempts']), 
                            correctposition=correctpositiondigits, wrongposition=wrongpositiondigits)

    
    if session['attempts'] == 0 and not session['startedgame']:
        answercode = ""
        for i in range(4):
            answercode += str(random.randint(0, 9))
        session["answer"] = answercode
    session['attempts'] += 1 if guess != 'None' or not validated else 0
    session['startedgame'] = True
    print(f"guess: {guess}  attempts: {session['attempts']}")

    
    return render_template('game_pages/gamepage.html', form=form, answer=session['answer'], attempts=max(1,session['attempts']), 
                            correctposition=correctpositiondigits, wrongposition=wrongpositiondigits)





    









