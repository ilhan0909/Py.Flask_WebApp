from flask import render_template, Blueprint, request, url_for, flash, redirect, abort
from flaskweb.models import User, Post

main = Blueprint('main', __name__)


@main.route('/')

#################HOME#########################


@main.route('/home')
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template("home.html", posts=posts)

###########################ABOUT####################################


@main.route('/about')
def about():
    return render_template("about.html", title="About")