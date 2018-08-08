from app.Dasshserver import DashServer
import dash_html_components as html

DashServer.layout = html.Div([
html.Div(id='graph-1')
])


@DashServer.callback(Output('graph-1', 'figure'), [Input('signal', 'children')])
def update_value_1(value):
    # generate_figure gets data from `global_store`.
    # the data in `global_store` has already been computed
    # by the `compute_value` callback and the result is stored
    # in the global redis cached
    return 'You have selected "{}"'.format(value)
