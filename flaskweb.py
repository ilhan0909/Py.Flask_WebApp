##start of flask framework webapp##

from flask import Flask, render_template, url_for
app = Flask(__name__)

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

if __name__ == "__main__":
    app.run(debug=True)