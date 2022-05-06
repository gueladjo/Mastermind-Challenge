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

# Page for User to choose level
@game.route('/dificulty', methods=['GET', 'POST'])
def chooselevel():
    #@ Review comment: Delete this unecessary white line
    return render_template('game_pages/levelpage.html')

# View page that runs the game
# Game difficulty is chosen based on passed parameter
@game.route('/startgame/<level>/mastermind', methods=['GET', 'POST'])
def startgame(level):

    # Initialize session dictionnary in order to store values based on cookies
    initializesession()
    isvalid, LIMIT = False, True
    hints, maxattempts = [], 10
   
    form = GuessingForm()  # User input form

    current_level = level 

    ############################## If user restarts page ############################################
    if request.method == 'POST':
        post_restart = request.form.get('restart')
        if post_restart is not None:
            resetdata()
            generatenumbercombination(gamesettings[current_level][0], gamesettings[current_level][1])
            return render_template('game_pages/gamepage.html', form=form, answer=session['answer'], attempts=max(0,maxattempts-session['attempts']), 
                            correctposition=0, wrongposition=0, digitlen=len(session['answer']), maxnum=gamesettings[current_level][1],hints=hints)





    userguess = form.guesscombo.data #Retrieve user input from Flask Forms
        #@ Review comment: This is correct but shouldn't it be else false instead of else isvalid. For clarity.
    isvalid = True if form.validate_guess(userguess, current_level) and userguess != 'None' else isvalid #isvalid boolean for string processing, changes criteria based on level parameter

    #@ Review comment: This should be moved after the next block that checks isvalid. Because if input is not valid you are executing the hints code without
    #@ reason.
    if session['startedgame'] == True:
        hints = gethints()
        print(hints)

    ############################ If Input passed by User is not valid #####################################
    if not isvalid and session['startedgame']: #Also checking for if game started as blank form when you first clicked on page is False per our above processing
        print("There is error in passed in guess")
        flash('Please enter a valid number combination!') 
        return render_template('game_pages/gamepage.html', form=form, answer=session['answer'], attempts=max(0,maxattempts-session['attempts']), 
                            correctposition=0, wrongposition=0, digitlen=len(session['answer']), maxnum=gamesettings[current_level][1], hints=hints)
    

    #@ Review comment: Similar to Settings case, it is better to use a class with explicit naming instead of digit: a class Position with parameters
    #@ position.reds and position.whites, which can be boolean for example. More clear than positions[0].
    positions = calculateposition(userguess) # Process which user input for correctness  ----> reds : whites
    correctposition = positions[0] if positions else 0
    wrongposition = positions[1] if positions else 0


    if isvalid: session['guesses'].append((userguess, correctposition, wrongposition)) # Save down previous valid user inputs for Hints
    
    
    print(f"Previous guesses are {session['guesses']}")
    print((userguess, session['answer'] if session['answer'] else ""))






    ############################# Notifiy User if they find correct answer and reinitilize/reset game state ##########################
    if isvalid and userguess == session['answer']: 
        print(f"You have found the correct positions in {session['attempts']} attempt(s)")
        score = calcultatescore()#####To implement later, we will also add to database in order to create leaderboard
        attempts = session['attempts']
        resetdata(restart=True)
        positions = (0, 0)
        flash('Congratulations, You have won the game in {} attempts(s)'.format(attempts + 1))
        return render_template('game_pages/gamepage.html', form=form, answer=session['answer'], attempts=max(0,maxattempts - attempts), 
                            correctposition=correctposition, wrongposition=wrongposition, digitlen=len(session['answer']), maxnum=gamesettings[current_level][1])
    
    ############################ If User exhausts Maximum attempts count #####################################
    elif LIMIT and maxattempts - session['attempts'] == 1 and userguess != session['answer']: #Also checking for if LIMIT mode is activated as well if User has raminingattempts
        flash('No more attempts left. Please restart game and try again!!!!') 
        return render_template('game_pages/gamepage.html', form=form, answer=session['answer'], attempts=max(0,maxattempts-session['attempts']), 
                            correctposition=0, wrongposition=0, digitlen=len(session['answer']), maxnum=gamesettings[current_level][1], hints=hints)

    
    print(f"Session attempts: {session['attempts']}        Has game started ? : {session['startedgame']}")










    ###########################Generate a new combination only when a new game (attempts==0) ##############################
    if session['attempts'] == 0 and not session['startedgame'] and not session['answer']:
        generatenumbercombination(gamesettings[current_level][0], gamesettings[current_level][1])

    

    session['attempts'] += 1 if isvalid else 0 # Only count valid attempts 
    session['startedgame'] = True # Change state of game to 'started'
    print(f"guess: {userguess}  attempts: {session['attempts']}")

    ##########################If we arrive here, we have not yet found the answer however our User input was valid ####################
    return render_template('game_pages/gamepage.html', form=form, answer=session['answer'], attempts=max(0,maxattempts-session['attempts']), 
                            correctposition=correctposition, wrongposition=wrongposition, digitlen=len(session['answer']), maxnum=gamesettings[current_level][1],hints=hints)





    









