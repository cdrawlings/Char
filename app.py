from flask import Flask, render_template, redirect, url_for, flash
from flask_mail import Mail, Message
from flask_sqlalchemy import SQLAlchemy

from config import Config
from forms import NewUser, NewChar

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
mail = Mail(app)


@app.route('/')
def index():
    msg = Message("Hello", sender='dev@rawlings.site', recipients=['c.d.rawlings@gmail.com'])
    msg.body = 'this is the test message'
    mail.send(msg)
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


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(debug=True)
