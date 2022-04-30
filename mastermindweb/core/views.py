from flask import render_template,request,Blueprint
from mastermindweb.models import BlogPost

core = Blueprint('core',__name__)

@core.route('/')
def index():

    return render_template('index.html')

@core.route('/info')
def info():

    return render_template('info.html')


@core.route('/blog')
def blog():

    page = request.args.get('page', 1, type=int)
    blog_posts = BlogPost.query.order_by(BlogPost.date.desc()).paginate(page=page, per_page=10)
    return render_template('viewblogposts.html',blog_posts=blog_posts)