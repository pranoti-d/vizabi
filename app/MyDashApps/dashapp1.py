from app.Dashserver import DashServer
from dash.dependencies import Input, State, Output
import dash_html_components as html
import dash
import dash_core_components as dcc


DashServer.layout = html.Div([
html.Div('Carrefour sales Viewer')
])

layout = DashServer.layout
