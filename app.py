from flask import Flask, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

from config import Config
from forms import NewUser

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


@app.route('/new_user', methods=('GET', 'POST'))
def newuser():
    form = NewUser()
    if form.validate_on_submit():
        flash('Login requested for user {}'.format(form.username.data, ))
        return redirect(url_for('/dashboard'))
    return render_template('new_user.html', title='create new user', form=form)


if __name__ == '__main__':
    app.run()
