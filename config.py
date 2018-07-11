import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
  ELASTICSEARCH_URL= 'http://localhost:9200'
  
