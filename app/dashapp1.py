from app.Dashserver import DashServer
import dash_html_components as html
from dash.dependencies import Input, State, Output
import dash
import dash_core_components as dcc
import urllib

DashServer.layout = html.Div([
html.Div(id='graph-1')
])


@DashServer.callback(Output('graph-1', 'children'), [Input('signal', 'children'),Input('url', 'pathname')])
def update_value_1(value, pathname):
    des = str(pathname) 
    filter = des.split('/')[-1]
    filter = urllib.parse.unquote(filter)
    return html.Div([
        html.H3('You are on page {}'.format(filter)) ])

layout = DashServer.layout
