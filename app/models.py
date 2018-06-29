from datetime import datetime
from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)
    
 class test_data_dummy_data(db.Model):
    Year = db.Column(db.Integer, primary_key=True)
    Metric = db.Column(db.String(129), primary_key=True)
    ANDHRA_PRADESH = db.Column(db.double))  	
    BIHAR = db.Column(db.double))  	
    CHHATTISGARH = db.Column(db.double))  	
    GUJARAT = db.Column(db.double))  	
    HARYANA = db.Column(db.double))  	
    HIMACHAL_PRADESH = db.Column(db.double))  	
    JHARKHAND = db.Column(db.double))  	
    KARNATAKA = db.Column(db.double))  	
    KERALA = db.Column(db.double))  	
    MADHYA_PRADESH = db.Column(db.double))  	
    MAHARASHTRA	= db.Column(db.double))  
    ORISSA = db.Column(db.double))  	
    PUNJAB = db.Column(db.double))  	
    RAJASTHAN = db.Column(db.double))  	
    TAMIL_NADU = db.Column(db.double))  	
    TELANGANA = db.Column(db.double))  	
    UTTAR_PRADESH = db.Column(db.double))  	
    WEST_BENGAL = db.Column(db.double))  	
    ALL_INDIA = db.Column(db.double))  

    def __repr__(self):
        return '<test_data_dummy_data {}>'.format(self.username)   
