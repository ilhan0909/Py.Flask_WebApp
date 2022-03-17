##start of flask framework webapp##
from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '3facec850363f99109512c58511bf1e7'

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
def homepage():
    return render_template("home.html", posts=posts)

@app.route('/about')
def about():
    return render_template("about.html", title="About")

@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template("register.html", title="Register", form="form")

@app.route('/login')
def login():
    form = LoginForm()
    return render_template("login.html", title="Login", form="form")

if __name__ == "__main__":
    app.run(debug=True)
