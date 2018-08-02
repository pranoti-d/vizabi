from app import app, db
from app.models import test_data_dummy_data, search_index
from app import server

@server.shell_context_processor
def make_shell_context():
    return {'db': db, 'test_data_dummy_data': test_data_dummy_data, 'search_index': search_index}


if __name__ == '__main__':
     app.run_server(debug=True)
