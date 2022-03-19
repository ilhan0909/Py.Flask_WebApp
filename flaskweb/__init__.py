from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '3facec850363f99109512c58511bf1e7'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

##routes should be imported after app initialisation.cuz we need to stop circular imports##

from flaskweb import routes
