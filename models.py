from datetime import datetime
from config import db, ma

class Contact(db.Model):
    __tablename__ = 'contacts'
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(32), index=True)
    noHp = db.Column(db.String(32))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class ContactSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Contact
        sqla_session = db.session 