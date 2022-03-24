from flask import request
from flask_restful import Resource
from models.model import ModelModel
from schemas.model import ModelSchema
from libs.strings import gettext

model_schema = ModelSchema()
model_list_schema = ModelSchema(many=True)

class Model(Resource):
    @classmethod
    def get(cls, name: str):
        model = ModelModel.find_by_name(name)
        if model:
            return model_schema.dump(model), 200

        return {"message": gettext("store_not_found")}, 404

    @classmethod
    def post(cls):
        model_json = request.get_json()
        model = model_schema.load(model_json)

        if ModelModel.find_by_name(model.name):
            return {"message": gettext("store_name_exists").format(model.name)}, 400
        
        try:
            model.save_to_db()
        except:
            return {"message": gettext("store_error_inserting")}, 500

        return model_schema.dump(model), 201

    @classmethod
    def delete(cls, name: str):
        model = ModelModel.find_by_name(name)
        if model:
            model.delete_from_db()
            return {"message": gettext("store_deleted")}, 200

        return {"message": gettext("store_not_found")}, 404


class ModelList(Resource):
    @classmethod
    def get(cls):
        return {"make": model_list_schema.dump(ModelModel.find_all())}, 200