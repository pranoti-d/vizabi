
# coding: utf-8

# In[ ]:


from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://qhcqehiqlrpqpj:02e86456526e31609afb17566ca32e34fb6b9cdc6b5ba70277584d43772bed0d@ec2-54-83-59-120.compute-1.amazonaws.com:5432/dcbk6mp1feuj2m'

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

