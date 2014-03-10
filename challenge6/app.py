from flask import Flask, request, render_template
from string import upper
from random import random, shuffle
from copy import deepcopy
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '[User: %r, Email:%r]' % (self.username, self.email)

@app.route('/home/')
def home():

    navigation = [
        {'href':'http://cnn.com', 'caption':'CNN', 'separator':'||'},
        {'href':'http://twitter.com', 'caption':'Twitter', 'separator':'||'},
        {'href':'http://facebook.com', 'caption':'Facebook', 'separator':''},
    ]

    return render_template('minimal_template.html', navigation=navigation,
                           a_variable='Welcome to My Webpage')

@app.route('/users/')
def users():
    return str(User.query.all())

@app.route('/users_template/')
def users_template():

    users = User.query.all()

    return render_template('users_template.html', users=users)

if __name__ == "__main__":
    app.run()
