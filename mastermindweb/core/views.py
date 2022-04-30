##Creates/updates users with the use of forms 

from flask import render_template,request,Blueprint
from mastermindweb.models import BlogPost

core = Blueprint('core',__name__)

##Homepage
@core.route('/')
def index():

    return render_template('index.html')


##General information about the game
@core.route('/info')
def info():

    return render_template('info.html')