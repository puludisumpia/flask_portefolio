from datetime import datetime

from applications import db

class Contact(db.Model):
    __tablename__ = "contacts"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow())

    def __str__(self):
        return self.name

