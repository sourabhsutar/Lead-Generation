from resources import vechicle
from ma import ma
from models.make import MakeModel
from models.vechicle import VechicleModel
from models.model import ModelModel

class MakeSchema(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = MakeModel
        load_only = ("creation_datetime","last_update")
        dump_only = ("id",)
        include_fk = True
        load_instance=True