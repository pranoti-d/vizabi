from datetime import datetime
#from app import db


class test_data_dummy_data(db.Model):
       Year = db.Column(db.Integer,index=True,primary_key=True)
        Month = db.Column(db.Integer,index=True)
        Week = db.Column(db.String(120),index=True)
        Frequency = db.Column(db.String(120),index=True)
        Date = db.Column(db.Date,index=True)
        Datetime = db.Column(db.String(120))
        Category = db.Column(db.String(120))
        Sub_Category = db.Column(db.String(120))
        Metric = db.Column(db.String(120), index=True)
        Units = db.Column(db.String(120))
	Source = db.Column(db.String(120))
	Description = db.Column(db.String(500))
	Remarks = db.Column(db.String(500))
	Tag = db.Column(db.String(120))
	CHANDIGARH = db.Column(db.Float)
	HARYANA = db.Column(db.Float)
	HIMACHAL_PRADESH = db.Column(db.Float)
	JAMMU_KASHMIR = db.Column(db.Float)
	NCT_OF_DELHI = db.Column(db.Float)
	PUNJAB = db.Column(db.Float)
	RAJASTHAN = db.Column(db.Float)
	ARUNACHAL_PRADESH = db.Column(db.Float)
	ASSAM = db.Column(db.Float)
	MANIPUR = db.Column(db.Float)
	MEGHALAYA = db.Column(db.Float)
	MIZORAM = db.Column(db.Float)
	NAGALAND = db.Column(db.Float)
	TRIPURA = db.Column(db.Float)
	ANDAMAN_NICOBAR_ISLANDS = db.Column(db.Float)
	BIHAR = db.Column(db.Float)
	JHARKHAND = db.Column(db.Float)
	ODISHA = db.Column(db.Float)
	SIKKIM = db.Column(db.Float)
	WEST_BENGAL = db.Column(db.Float)
	CHHATTISGARH = db.Column(db.Float)
	MADHYA_PRADESH = db.Column(db.Float)
	UTTARAKHAND = db.Column(db.Float)
	UTTAR_PRADESH = db.Column(db.Float)
	DADRANAGAR_HAVELI = db.Column(db.Float)\=\
	DAMAN_DIU = db.Column(db.Float)
	GOA = db.Column(db.Float)
	GUJARAT = db.Column(db.Float)
	MAHARASHTRA = db.Column(db.Float)
	ANDHRA_PRADESH = db.Column(db.Float)
	KARNATAKA = db.Column(db.Float)
	KERALA = db.Column(db.Float)
	LAKSHADWEEP = db.Column(db.Float)
	PUDUCHERRY = db.Column(db.Float)
	TAMIL_NADU = db.Column(db.Float)
	TELANGANA = db.Column(db.Float)
	All_India = db.Column(db.Float)


    def __repr__(self):
        return '<test_data_dummy_data {}>'.format(self.Metric)

    

