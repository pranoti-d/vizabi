from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_mysqldb import MySQL
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = MySQL(app)
migrate = Migrate(app, db)

from app import routes, models
