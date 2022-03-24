from flask_restful import Resource
from models.vechicle import VechicleModel
from schemas.vechicle import VechicleSchema
from libs.strings import gettext

vechicle_schema = VechicleSchema()
vechicle_list_schema = VechicleSchema(many=True)

class Vechicle(Resource):
    @classmethod
    def get(cls, name: str):
        vechicle = VechicleModel.find_by_name(name)
        if vechicle:
            return vechicle_schema.dump(vechicle), 200

        return {"message": gettext("store_not_found")}, 404

    @classmethod
    def post(cls, name: str):
        if VechicleModel.find_by_name(name):
            return {"message": gettext("store_name_exists").format(name)}, 400

        vechicle = VechicleModel(name=name)
        try:
            vechicle.save_to_db()
        except:
            return {"message": gettext("store_error_inserting")}, 500

        return vechicle_schema.dump(vechicle), 201

    @classmethod
    def delete(cls, name: str):
        vechicle = VechicleModel.find_by_name(name)
        if vechicle:
            vechicle.delete_from_db()
            return {"message": gettext("store_deleted")}, 200

        return {"message": gettext("store_not_found")}, 404


class VechicleList(Resource):
    @classmethod
    def get(cls):
        return {"vechicle": vechicle_list_schema.dump(VechicleModel.find_all())}, 200