##start of flask framework webapp##

from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def homepage():
    return '<h1>Welcome to Home Page!</h1>'

@app.route('/about')
def about():
    return '<h1>Welcome to About Page!</h1>'

if __name__ == "__main__":
    app.run(debug=True)