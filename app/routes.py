from app import app
from app import server

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"
