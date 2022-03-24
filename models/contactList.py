import datetime
from db import db
from typing import List

class contactListModel(db.Model):
    __tablename__ = "contact_list"

    id = db.Column(db.Integer, primary_key=True)
    contact_id = db.Column(db.Integer, db.ForeignKey('contact.id'))
    main_list_id = db.Column(db.Integer, db.ForeignKey('contactMainList.id'))
    creation_datetime = db.Column(db.DateTime,default=datetime.datetime.utcnow)
    last_update = db.Column(db.DateTime)