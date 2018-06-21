
# coding: utf-8

# In[ ]:


from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://jnlvmsknzpwzhn:4c833c22f02531350c227cf49d5d823a5cf7f0d5fd03029228623fd35bf12be9@ec2-107-21-255-2.compute-1.amazonaws.com:5432/del813fhfj7fn9'

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

