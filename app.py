
# coding: utf-8

# In[ ]:


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
os.environ.get('DATABASE_URL')

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)

from models import User

@app.route('/add/')
def webhook():
    name = "ram"
    email = "ram@ram.com"
    u = User(id = id, nickname = name, email = email)
    print("user created", u)
    db.session.add(u)
    db.session.commit()
    return "user created"

@app.route('/delete/')
def delete():
    u = User.query.get(i)
    db.session.delete(u)
    db.session.commit()
    return "user deleted"

if __name__ == '__main__':
    app.run()

