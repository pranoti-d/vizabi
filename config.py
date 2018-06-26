import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    MYSQL_HOST = 'us-cdbr-iron-east-04.cleardb.net'
    MYSQL_USER = 'bd41fb7755cb95'
    MYSQL_PASSWORD = 'e89a06f5'
    MYSQL_DB = 'heroku_d45ae70ddfab245'
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://bd41fb7755cb95:e89a06f5@us-cdbr-iron-east-04.cleardb.net/heroku_d45ae70ddfab245'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
  
