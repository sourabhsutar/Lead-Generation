from ma import ma
from models.model import ModelModel
from models.make import MakeModel

class ModelSchema(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = ModelModel
        load_only = ("creation_datetime","last_update")
        dump_only = ("id",)
        include_fk = True
        load_instance=True