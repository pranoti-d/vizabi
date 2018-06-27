from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_mysqldb import MySQL
from flask_migrate import Migrate

#app = Flask(__name__)
server = flask.Flask(__name__)
app = dash.Dash(__name__, server=server)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models
