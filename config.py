import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    ELASTICSEARCH_URL= 'http://localhost:9200'
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'passowrd'
    MYSQL_DB = 'db'
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql:/root:password@localhost/db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
  
