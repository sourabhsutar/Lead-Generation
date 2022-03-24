from flask import request
from flask_restful import Resource
from models.make import MakeModel
from schemas.make import MakeSchema
from libs.strings import gettext

make_schema = MakeSchema()
make_list_schema = MakeSchema(many=True)

class Make(Resource):
    @classmethod
    def get(cls, name: str):
        make = MakeModel.find_by_name(name)
        if make:
            return make_schema.dump(make), 200

        return {"message": gettext("store_not_found")}, 404

    @classmethod
    def post(cls):
        make_json = request.get_json()
        make = make_schema.load(make_json)

        if MakeModel.find_by_name(make.name):
            return {"message": gettext("store_name_exists").format(make.name)}, 400
        
        try:
            make.save_to_db()
        except:
            return {"message": gettext("store_error_inserting")}, 500

        return make_schema.dump(make), 201

    @classmethod
    def delete(cls, name: str):
        make = MakeModel.find_by_name(name)
        if make:
            make.delete_from_db()
            return {"message": gettext("store_deleted")}, 200

        return {"message": gettext("store_not_found")}, 404


class MakeList(Resource):
    @classmethod
    def get(cls):
        
        makeModelObj = MakeModel.find_all()
        dataList = []
        for data in makeModelObj:
            dataList.append({'id':data.id,'name':data.name,'vechicle_name':data.vechicle.name})
        
        return {"make": make_list_schema.dump(dataList)}, 200