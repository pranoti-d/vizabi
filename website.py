from app import app, db
from app.models import test_data_dummy_data
#from app import server

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'test_data_dummy_data': test_data_dummy_data}
