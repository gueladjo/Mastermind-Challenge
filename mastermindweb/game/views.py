from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from mastermindweb import db


game = Blueprint('game', __name__)

@game.route('/dificulty', methods=['GET', 'POST'])
def chooselevel():
    
    return render_template('game_pages/levelpage.html')

