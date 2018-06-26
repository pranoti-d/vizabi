import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://bd41fb7755cb95:e89a06f5@us-cdbr-iron-east-04.cleardb.net/heroku_d45ae70ddfab245?reconnect=true'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
