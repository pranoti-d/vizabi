from datetime import datetime
#from app import db


class test_data_dummy_data(db.Model):
    Year = db.Column(db.Integer,index=True,primary_key=True)
    Month = db.Column(db.Integer,index=True)
    Week = db.Column(db.String(120),index=True)
    Date = db.Column(db.Date,index=True)
    Datetime = db.Column(db.String(120))
    Category = db.Column(db.String(120))
    Metric = db.Column(db.String(120), index=True)
    Units = db.Column(db.String(120))
    ANDHRA_PRADESH = db.Column(db.Float)	
    BIHAR = db.Column(db.Float)		
    CHHATTISGARH = db.Column(db.Float)		
    GUJARAT = db.Column(db.Float)		
    HARYANA	= db.Column(db.Float)	
    HIMACHAL_PRADESH = db.Column(db.Float)		
    JHARKHAND = db.Column(db.Float)		
    KARNATAKA = db.Column(db.Float)		
    KERALA = db.Column(db.Float)		
    MADHYA_PRADESH	= db.Column(db.Float)
    MAHARASHTRA	= db.Column(db.Float)
    ORISSA	= db.Column(db.Float)
    PUNJAB	= db.Column(db.Float)
    RAJASTHAN = db.Column(db.Float)	
    TAMIL_NADU	= db.Column(db.Float)
    TELANGANA = db.Column(db.Float)	
    UTTAR_PRADESH = db.Column(db.Float)	
    WEST_BENGAL	= db.Column(db.Float)
    ALL_INDIA = db.Column(db.Float)

    def __repr__(self):
        return '<test_data_dummy_data {}>'.format(self.Metric)

    

