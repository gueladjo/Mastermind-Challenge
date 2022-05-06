import random
from mastermindweb import app
from flask import Flask, session
from flask_session import Session
from flask import render_template, url_for, flash, redirect, request, Blueprint
from collections import namedtuple
#@ Review comment: Try to clean up all the unecessary white lines in your files. In most cases one white line is enough.



gaming = Blueprint('game', __name__)
SESSION_TYPE = 'filesystem'
###Remove if causes bugs
app.config.from_object(__name__)

#To share data between requests, we can store data in a session instead of having to store in a database
#A session makes it possible to remember information from one request to another. The way Flask does this is by using a signed cookie
Session(app)



#Create namedtuple in order to store hints
Hints = namedtuple('Hints', ['userguess', 'correctcount', 'wrongcount'])

#@ Review comment: This would usually be done with a class Settings that has public members number of digits and number of combinations. You would
#@ use it like gamesettings['easy'].number_of_digits which is clearer than gamesettings['easy'][0] where it is not clear what 0 really represents.
#@ Also total number of available digit is supposed to be 8 by default not 7 so would recommend making it 8 here and modifying generatenumbercombination to use
#@ numberofcombination - 1 instead. It makes it clearer.
# sets combination settings and criterias 
gamesettings = {'easy': [4, 7], 'medium':[5, 7], 'hard':[8, 10]}


def resetdata(restart=False):
    session['attempts'] = 0
    session['answer']= ""
    session['guesses'] = []
    session['level'] = ''
    if not restart:
        session['startedgame'] = False #Handles behavior for restart

def initializesession():
    if "answer" not in session:
        session["answer"]= ""
    if "attempts" not in session:
        session["attempts"] = 0
    if 'guesses' not in session:
        session['guesses'] = []
    if 'startedgame' not in session:
        session['startedgame'] = False
    if 'level' not in session:
        session['level'] = ''
    
#@ Review comment: delete this if it is not implemented.    
# Will evaluate User's Performance by assigning them a score 
def calcultatescore():
    pass
#@ Review comment: add a white line to separate the two functions    
# Find RED and WHITE pins
def calculateposition(userguess):
    reds, whites = 0, 0
    if not session['answer'] or not userguess: return (0, 0)

    answer, guess = session['answer'], userguess
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




# Combination length --> represents how many digits combination can contain
# numberofcombination --> represesents the total different numbers combination can have
def generatenumbercombination(combinationlen, numberofcombination):
    codecombination = ""
    #@ Review comment: Are you using the http API they tell you to use in the project plan ? This looks like default Python random API.
    for i in range(combinationlen):
        codecombination += str(random.randint(0, numberofcombination))
    
    #Add response key to session
    session["answer"] = codecombination

# Get hints in decreasing order of total position found #
# Format: List:tuple:[(userguess, correctpos, wrongpos)]
def gethints():
    return sorted(session['guesses'], key=lambda x: x[1] + x[2], reverse=True)
                

