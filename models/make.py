import datetime
from db import db
from typing import List


class MakeModel(db.Model):
    __tablename__ = "make"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(88))
    vechicle_id = db.Column(db.Integer,db.ForeignKey('vechicle.id'))
    creation_datetime = db.Column(db.DateTime,default=datetime.datetime.utcnow)
    last_update = db.Column(db.DateTime)

    vechicle = db.relationship("VechicleModel", backref='vechicle',uselist=False)

    def __init__(self, name: str, vechicle_id: int, vechicle_name: str):
        self.name = name
        self.vechicle_id = vechicle_id
        self.vechicle_name = vechicle_name

    @classmethod
    def find_by_id(cls, _id: int) -> "MakeModel":
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_by_name(cls, _name: str) -> "MakeModel":
        return cls.query.filter_by(name=_name).first()

    @classmethod
    def find_all(cls) -> List["MakeModel"]:
        return cls.query.all()

    def save_to_db(self) -> int:
        db.session.add(self)
        db.session.commit()
        db.session.refresh(self)
        return self.id


    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
