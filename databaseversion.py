from app import server
from app import app

import dash
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
from bisect import bisect_left
from datetime import datetime
from copy import deepcopy
import plotly.graph_objs as go
from flask import Flask, render_template
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_mysqldb import MySQL
from flask_migrate import Migrate

server = Flask(__name__)
app = dash.Dash(__name__, server=server, static_folder='assets')


server.config.from_object(Config)
db = SQLAlchemy(server)
migrate = Migrate(server, db)
cursor = db.cursor()
cursor.execute("SELECT * from test_data_dummy_data")
data = cursor.fetchone()

# In[2]:


file = pd.read_csv( "Test Data_Dummy Data.csv", encoding = "ISO-8859-1")
file.iloc[:,2:20] = file.iloc[:,2:20].apply(lambda x : round(x, 2))


# In[ ]:


def select_chart(x_axis,y_axis,chart_type) :
    data_chart = file
    dataPanda = create_trace(data_chart,x_axis,y_axis,chart_type)
    return dataPanda
     
    
def create_trace(data_chart,x_axis,y_axis,chart_type) :    
    dataPanda = []
    for i in data_chart.iloc[:,2:20].columns.unique():
        trace = go.Scatter(
                    x=data_chart[data_chart['Metric'] == x_axis][i],
                    y=data_chart[data_chart['Metric'] == y_axis][i],
                    text= i,
                    mode='markers',
                    opacity=0.7,
                    marker={
                        'size': 15,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                    name=i  ) 
        dataPanda.append(trace)
    return dataPanda
    
def create_layout(x_axis,y_axis) : 
    layout =  go.Layout(
               # autosize=False,
               # width=1000,
                height=700,
                xaxis = dict(type = 'log', title= x_axis),
                yaxis=dict(title=y_axis),
                legend=dict(orientation="h"),
                hovermode='closest'
            )
    return layout


# In[ ]:


#app = dash.Dash(__name__, static_folder='assets')
# app.scripts.config.serve_locally=True
# app.css.config.serve_locally=True
# app.config.supress_callback_exceptions=True


#app = dash.Dash(__name__, server=server, static_folder='assets')


app.css.append_css({'external_url':
#                 'https://cdn.rawgit.com/gschivley/8040fc3c7e11d2a4e7f0589ffc829a02/raw/fe763af6be3fc79eca341b04cd641124de6f6f0d/dash.css'
                  'https://cdn.rawgit.com/plotly/dash-app-stylesheets/2d266c578d2a6e8850ebce48fdb52759b2aef506/stylesheet-oil-and-gas.css'
               })
app.title = 'States of India'
#server = app.server

app.layout = html.Div([
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
    
    # selectors
   html.Div(
        [ 
     html.Div(
        [
            html.P('Choose x-axis:'), 
            dcc.Dropdown(
                    id='x_axis',
                    options=[{'label': 'Real GDP Growth', 'value': 'Real GDP Growth'},
                             {'label': 'Per capita GDP', 'value': 'Per capita GDP'},
                             {'label': 'Population', 'value': 'Population'}],              
                    value='Per capita GDP'
                        )
            ],
           className='four columns',
           style={'margin-top': '10'}
     ),
    
    html.Div(
        [
            html.P('Choose y-axis:'), 
            dcc.Dropdown(
                    id='y_axis',
                    options=[{'label': 'Real GDP Growth', 'value': 'Real GDP Growth'},
                             {'label': 'Per capita GDP', 'value': 'Per capita GDP'},
                             {'label': 'Population', 'value': 'Population'}],              
                    value='Population'
                        )
            ],
           className='four columns',
           style={'margin-top': '10'}
     ),
    
       html.Div(
        [
            html.P('Choose chart-type:'), 
            dcc.Dropdown(
                    id='chart_type',
                    options=[{'label': 'Scatter', 'value': 'scatter'}],              
                    value='scatter'
                        )
            ],
           className='four columns',
           style={'margin-top': '10'}
     )
        ], className='row'
   ),
    
  #chart
     html.Div(
        [
            dcc.Graph(id='example-graph',
                              animate=True, 
                              style={'margin-top': '20'},
                               config={'displayModeBar': False}
                     )
        ], className='row'
         ),
    
    dcc.Markdown('Created by [Ashutosh Datar](https://twitter.com/adatar)')
   
], className='ten columns offset-by-one')    

@app.callback(
    dash.dependencies.Output('example-graph', 'figure'),
    [dash.dependencies.Input('x_axis', 'value'),
    dash.dependencies.Input('y_axis', 'value'),
    dash.dependencies.Input('chart_type', 'value'),
    ])
def update_output(x_axis, y_axis, chart_type):
    dataPanda = select_chart(x_axis,y_axis,chart_type)
    layout = create_layout(x_axis,y_axis)
    figure = {'data': dataPanda,
            'layout': layout}
    return figure  
    

if __name__ == '__main__':
    app.run_server(debug=True)
