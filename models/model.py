import datetime
from db import db
from typing import List


class ModelModel(db.Model):
    __tablename__ = "model"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(88))
    make_id = db.Column(db.Integer,db.ForeignKey('make.id'))
    creation_datetime = db.Column(db.DateTime,default=datetime.datetime.utcnow)
    last_update = db.Column(db.DateTime)

    makeObj = db.relationship("MakeModel", backref='make1',uselist=False)

    @classmethod
    def find_by_id(cls, _id: int) -> "ModelModel":
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_by_name(cls, _name: str) -> "ModelModel":
        return cls.query.filter_by(name=_name).first()

    @classmethod
    def find_all(cls) -> List["ModelModel"]:
        return cls.query.all()

    def save_to_db(self) -> int:
        db.session.add(self)
        db.session.commit()
        db.session.refresh(self)
        return self.id


    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
