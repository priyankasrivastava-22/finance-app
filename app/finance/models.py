# Defines Transaction table structure

from app.database import db

class Transaction(db.Model):
    # Primary key
    id = db.Column(db.Integer, primary_key=True)

    # income or expense
    type = db.Column(db.String(20), nullable=False)

    # category like food, rent etc.
    category = db.Column(db.String(100), nullable=False)

    # amount value
    amount = db.Column(db.Float, nullable=False)