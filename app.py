from flask import Flask, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

from config import Config
from forms import NewUser, NewChar

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


@app.route('/new_character', methods=('GET', 'POST'))
def newchar():
    form = NewChar()
    if form.validate_on_submit():
        return redirect(url_for('dashboard'))
    return render_template('new_char.html', title='Create new character', form=form)


@app.route('/new_user', methods=('GET', 'POST'))
def newuser():
    form = NewUser()
    if form.validate_on_submit():
        flash('Login requested for user {}'.format(form.name.data, ))
        return redirect(url_for('dashboard'))
    return render_template('new_user.html', title='create new user', form=form)


if __name__ == '__main__':
    app.run(debug=True)
