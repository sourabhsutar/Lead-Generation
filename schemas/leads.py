from ma import ma
from models.leads import LeadsModel
from schemas.make import MakeSchema

class LeadsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = LeadsModel
        load_only = ("id",)
        dump_only = ("id",)
        load_instance=True
        include_fk = True