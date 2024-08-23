from app import db
from datetime import datetime
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    user_id = db.Column(db.String(20), unique=True)
    password_hash = db.Column(db.String(128))
    section = db.Column(db.String(64))
    user_type = db.Column(db.String(20))  # Admin, shop floor, PCO

    def __repr__(self):
        return f'<User {self.username}>'

class Workorder(db.Model):
    workorder_no = db.Column(db.String(20), primary_key=True)
    workorder_date = db.Column(db.Date, default=datetime.utcnow)
    item_name = db.Column(db.String(50), db.ForeignKey('item.item_name'))
    consignee = db.Column(db.String(50), db.ForeignKey('consignee.consignee'))
    allocation_no = db.Column(db.String(50))
    quantity = db.Column(db.Integer)
    job_number = db.Column(db.String(8), unique=True)
    workorder_status = db.Column(db.String(10), default='active')

    def __repr__(self):
        return f'<Workorder {self.workorder_no}>'

class Consignee(db.Model):
    zone = db.Column(db.String(50))
    division = db.Column(db.String(50))
    indenter = db.Column(db.String(50))
    consignee = db.Column(db.String(50), primary_key=True)
    consignee_type = db.Column(db.String(50))  # Home Revenue, Projects, Construction

    def __repr__(self):
        return f'<Consignee {self.consignee}>'

class Item(db.Model):
    item_name = db.Column(db.String(50), primary_key=True)
    item_description = db.Column(db.String(100))
    item_type = db.Column(db.String(20))  # SG or NSG
    sg_number = db.Column(db.String(20), nullable=True)

    def __repr__(self):
        return f'<Item {self.item_name}>'