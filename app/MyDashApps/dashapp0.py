from app.Dashserver import DashServer
from dash.dependencies import Input, State, Output
import dash_html_components as html
import dash
import dash_core_components as dcc
import pandas as pd
from bisect import bisect_left
from datetime import datetime
from copy import deepcopy
import plotly.graph_objs as go
from flask import Flask, render_template
from app.server import db
from app.models import test_data_dummy_data
from app.MyDashApps import dashapp1





DashServer.css.append_css({'external_url':

#                 'https://cdn.rawgit.com/gschivley/8040fc3c7e11d2a4e7f0589ffc829a02/raw/fe763af6be3fc79eca341b04cd641124de6f6f0d/dash.css'

                  'https://cdn.rawgit.com/plotly/dash-app-stylesheets/2d266c578d2a6e8850ebce48fdb52759b2aef506/stylesheet-oil-and-gas.css'

               })

DashServer.title = 'States of India'

#server = app.server



DashServer.layout = html.Div([

    # title row

    html.Div(

        [

            html.H1(

                'States of India',

                style={'font-family': 'Helvetica',

                       "margin-top": "25",

                       "margin-bottom": "0"},

                className='eight columns',

            ),

             html.P(

                'Explore states of India',

                style={'font-family': 'Helvetica',

                       "font-size": "120%",

                       "width": "80%"},

                className='eight columns',

            ),

        ], 

         className='row'

        ),

    

    # Select visualization

    

     html.Div(

        [

             html.Label('What would you like to visualize?'),

                 dcc.Dropdown(
                    id = 'app-1-dropdown', 
                    options=[

                        {'label': 'Economy', 'value': 'NYC'},

                        {'label': 'Banking', 'value': 'MTL'},

                        {'label': 'States', 'value': 'SF'}

                            ],

                     value=['MTL', 'SF'],

                     multi=True

                             ),
                  dcc.Link('Search', href='/app/MyDashApps/dashapp1')

         ], 
       
         className='row'

        ),

  
  

], className='ten columns offset-by-one')    



layout = DashServer.layout

@DashServer.callback(
    Output('page-content1', 'children'),
     [Input('btn_1', 'n_clicks')])
def update_output(n_clicks):
    return redirect('/app/MyDashApps/dashapp1')
   

