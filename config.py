import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://rawlings:5eDnD@localhost:8889/char"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.rawlings.site'
    MAIL_PORT = 587
    MAIL_USE_TLS = True,
    MAIL_USERNAME = 'dev@rawlings.site'
    MAIL_PASSWORD = 'Test1Test'
    MAIL_DEBUG = False
    MAIL_SUPPRESS_SEND = False
    TESTING = False
    # MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    # MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
