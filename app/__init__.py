from flask import Flask, render_template
#from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_mysqldb import MySQL
from flask_migrate import Migrate
from dash import Dash
from dash.dependencies import Input, State, Output
import dash_core_components as dcc
import dash_html_components as html

import json
import plotly
import pandas as pd
import numpy as np


app = Flask(__name__)
#server = Flask(__name__)
#app = Dash(__name__, server=server, url_base_pathname='/dashed') #Another Bash Graph inline, no callbacks.
#app = dash.Dash(__name__, server=server)
#app.config.from_object(Config)

#server.config.from_object(Config)
#db = SQLAlchemy(server)
#migrate = Migrate(server, db)

#from app import routes, models
from app import routes
