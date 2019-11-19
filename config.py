import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://rawlings:5eDnD@localhost:8889/char"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
