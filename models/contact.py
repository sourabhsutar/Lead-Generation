import datetime
from db import db


class ContactModel(db.Model):
    __tablename__ = "contact"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(88))
    last_name = db.Column(db.String(88))
    email = db.Column(db.String(88))
    phone_number = db.Column(db.String(88))
    zipcode = db.Column(db.String(88))
    vechile_type = db.Column(db.Integer,db.ForeignKey('vechicle.id'))
    make = db.Column(db.Integer,db.ForeignKey('make.id'))
    model = db.Column(db.Integer,db.ForeignKey('model.id'))
    creation_datetime = db.Column(db.DateTime,default=datetime.datetime.utcnow)
    last_update = db.Column(db.DateTime)

    makeObj = db.relationship("MakeModel", backref='make1',uselist=False)

    @classmethod
    def find_by_id(cls, _id: int) -> "ContactModel":
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_by_name(cls, _name: str) -> "ContactModel":
        return cls.query.filter_by(name=_name).first()

    @classmethod
    def find_all(cls) -> List["ContactModel"]:
        return cls.query.all()

    def save_to_db(self) -> int:
        db.session.add(self)
        db.session.commit()
        db.session.refresh(self)
        return self.id


    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
