import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    TOKEN = 'b69168e0d54c44e108922619d8ea1bac88d18ced'
    USERNAME = 'procon'
    PASSWORD = 'HobOnset8!'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
