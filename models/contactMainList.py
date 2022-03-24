import datetime
from db import db
from typing import List

class contactMainList(db.Model):
    __tablename__ = "contact_main_list"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(88))
    description = db.Column(db.Text())
    total_contact = db.Column(db.Integer)
    status = db.Column(db.Boolean)
    creation_datetime = db.Column(db.DateTime,default=datetime.datetime.utcnow)
    last_update = db.Column(db.DateTime)