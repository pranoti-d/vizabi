from dashserver import DashServer

DashServer.layout = html.Div([
	dcc.Location(id='url', refresh=False),
	html.Div(id='page-content')
	])

@DashServer.callback(Output('page-content', 'children'),[Input('url', 'pathname')])
def display_page(pathname):
	if pathname == '/app/':
