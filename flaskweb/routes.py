from flask import render_template, url_for, flash, redirect
from flaskweb.models import User, Post
from flaskweb.forms import RegistrationForm, LoginForm
from flaskweb import app

posts = [
    {
        'author' : 'İlhan Bayramoğlu',
        'title' : 'First Blog Post',
        'content' : 'Content of First Blog Post',
        'date_posted' : 'March 5, 2022'
    },
    {
        'author' : 'Rabia',
        'title' : 'Second Blog Post',
        'content' : 'Content of Second Blog Post',
        'date_posted' : 'March 6, 2022'
    }

]

@app.route('/')

@app.route('/home')
def home():
    return render_template("home.html", posts=posts)

@app.route('/about')
def about():
    return render_template("about.html", title="About")

@app.route('/register', methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template("register.html", title="Register", form=form)

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@blog.com" and form.password.data == "password":
            flash('You have been logged in! ', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login failed,check your info!', 'danger')
    return render_template("login.html", title="Login", form=form)