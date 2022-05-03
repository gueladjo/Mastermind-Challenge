from tracemalloc import start
from turtle import position
from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from mastermindweb.game.gaming import generatenumbercombination, initializesession, resetdata, calcultatescore, calculateposition, Hints, gethints
from mastermindweb.game.gaming import generatenumbercombination, gamesettings
from mastermindweb.game.forms import GuessingForm
from flask_restful import abort
from mastermindweb import db
from mastermindweb import app
from flask import Flask, session

game = Blueprint('game', __name__)
##########Store guesses in set#########


@game.route('/dificulty', methods=['GET', 'POST'])
def chooselevel():
    
    return render_template('game_pages/levelpage.html')


@game.route('/startgame/mastermind', methods=['GET', 'POST'])
def startgame():
    ###########Adding values to keys to prevent key errors###########
    initializesession()
    startedgame, isvalid = False, False

    ####Save user input into guess variable#####
    form = GuessingForm()

    current_level = 'easy'

    if request.method == 'POST':
        post_restart = request.form.get('restart')
        if post_restart is not None:
            resetdata()
            generatenumbercombination(gamesettings[current_level][0], gamesettings[current_level][1])
            return render_template('game_pages/gamepage.html', form=form, answer=session['answer'], attempts=max(0,session['attempts']), 
                            correctposition=0, wrongposition=0)



    userguess = form.guesscombo.data
    isvalid = True if form.validate_guess(userguess, current_level) and userguess != 'None' else isvalid


    #print(f"These are the forms {validated}")
    if not isvalid and session['startedgame']: 
        print("There is error in passed in guess")
        flash('Please enter a valid number combination!') 
        return render_template('game_pages/gamepage.html', form=form, answer=session['answer'], attempts=max(1,session['attempts']), 
                            correctposition=0, wrongposition=0)

    positions = calculateposition(userguess)
    correctposition = positions[0] if positions else 0
    wrongposition = positions[1] if positions else 0


    if isvalid: session['guesses'].append(Hints(userguess, correctposition, wrongposition))
    print(f"Previous guesses are {session['guesses']}")

    print((userguess, session['answer'] if session['answer'] else ""))
    #######If we've found the answer##########################
    if isvalid and userguess == session['answer']: 
        print(f"You have found the correct positions in {session['attempts']} attempt(s)")
        score = calcultatescore()#####To implement later, we will also add to database in order to create leaderboard
        attempts = session['attempts']
        resetdata()
        positions = (0, 0)
        flash('Congratulations, You have won the game in {} attempts(s)'.format(attempts + 1))
        hints = gethints()
        print(hints)
        return render_template('game_pages/gamepage.html', form=form, answer=session['answer'], attempts=max(0,attempts), 
                            correctposition=correctposition, wrongposition=wrongposition)

    
    print(f"Session attempts: {session['attempts']}        Has game started ? : {session['startedgame']}")

    if session['attempts'] == 0 and not session['startedgame']:
        generatenumbercombination(gamesettings[current_level][0], gamesettings[current_level][1])

    session['attempts'] += 1 if isvalid else 0
    session['startedgame'] = True
    print(f"guess: {userguess}  attempts: {session['attempts']}")

    
    return render_template('game_pages/gamepage.html', form=form, answer=session['answer'], attempts=max(0,session['attempts']), 
                            correctposition=correctposition, wrongposition=wrongposition)





    









