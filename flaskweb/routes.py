import secrets, os
from PIL import Image
from flask import render_template, url_for, flash, redirect, request
from flaskweb.models import User, Post
from flaskweb.forms import RegistrationForm, LoginForm, UpdateAccountForm
from flaskweb import app, db, bcrypt
from flask_login import login_user, current_user, logout_user, login_required

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
    if current_user.is_authenticated:
        return redirect(url_for('home')), flash('You are already registered!', 'danger')
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You can now Login.', 'success')
        return redirect(url_for('login'))
    return render_template("register.html", title="Register", form=form)

@app.route('/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home')),flash('You are already logged in!', 'danger')
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login failed,please check your email and password!', 'danger')
    return render_template("login.html", title="Login", form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home')), flash('You successfully logged out!', 'success')

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    f_name, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)

##image file will be rescaled to 125*125 for data/storage saving purposes##
    output_size = (125,125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn

@app.route('/account',methods=['GET','POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been successfully updated!', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template("account.html", title="Account", image_file=image_file, form=form)








