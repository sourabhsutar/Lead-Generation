from sqlalchemy.orm import backref
from db import db


class LeadsModel(db.Model):
    __tablename__ = "leads"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False, unique=True)
    last_name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80))
    phone_number = db.Column(db.String(13))
    city = db.Column(db.String(80))
    website = db.Column(db.String(80))
    lead_id = db.Column(db.String(80))
    vechile_type = db.Column(db.Integer,db.ForeignKey('vechicle.id'))
    make = db.Column(db.Integer,db.ForeignKey('make.id'))
    model = db.Column(db.Integer,db.ForeignKey('model.id'))
    vin = db.Column(db.String(255))
    
  #  makeObj = db.relationship("MakeModel",backref='make',uselist=False)
    vechicleObj = db.relationship("VechicleModel", backref=' makeVechicle',uselist=False)
   # modelObj = db.relationship("ModelModel", backref=' model',uselist=False)

    @classmethod
    def find_by_email(cls, email: str) -> "LeadsModel":
        return cls.query.filter_by(email=email).first()

    @classmethod
    def find_by_name(cls,firstname: str) -> "LeadsModel":
        return cls.query.filter_by(first_name=firstname).first()

    @classmethod
    def find_by_id(cls, _id: int) -> "LeadsModel":
        return cls.query.filter_by(id=_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
        db.session.refresh(self)
        return self.id


    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
