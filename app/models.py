from datetime import datetime
from app import db


class User(db.Model):
    Year = db.Column(db.Integer,index=True)
    Metric = db.Column(db.Double, index=True)
    ANDHRA_PRADESH = db.Column(db.Double)	
    BIHAR = db.Column(db.Double)		
    CHHATTISGARH = db.Column(db.Double)		
    GUJARAT = db.Column(db.Double)		
    HARYANA	= db.Column(db.Double)	
    HIMACHAL_PRADESH = db.Column(db.Double)		
    JHARKHAND = db.Column(db.Double)		
    KARNATAKA = db.Column(db.Double)		
    KERALA = db.Column(db.Double)		
    MADHYA_PRADESH	= db.Column(db.Double)
    MAHARASHTRA	= db.Column(db.Double)
    ORISSA	= db.Column(db.Double)
    PUNJAB	= db.Column(db.Double)
    RAJASTHAN = db.Column(db.Double)	
    TAMIL_NADU	= db.Column(db.Double)
    TELANGANA = db.Column(db.Double)	
    UTTAR_PRADESH = db.Column(db.Double)	
    WEST_BENGAL	= db.Column(db.Double)
    ALL_INDIA = db.Column(db.Double)

    def __repr__(self):
        return '<User {}>'.format(self.Metric)

    

