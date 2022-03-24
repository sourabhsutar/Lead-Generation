from ma import ma
from models.vechicle import VechicleModel
#from models.leads import LeadsModel
#from schemas.leads import LeadsSchema

class VechicleSchema(ma.SQLAlchemyAutoSchema):
    #leads = ma.Nested(LeadsSchema, many=True)
    class Meta:
        model = VechicleModel
        load_only = ("creation_datetime","last_update")
        dump_only = ("id",)
        include_fk = True
        load_instance=True
