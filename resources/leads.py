from flask_restful import Resource
from flask import request
from werkzeug.security import safe_str_cmp
from werkzeug.wrappers import Response
from flask_jwt_extended import jwt_required
from models.leads import LeadsModel
from schemas.leads import LeadsSchema
from blacklist import BLACKLIST
from libs.strings import gettext

leads_schema = LeadsSchema()

class LeadsRegister(Resource):
    @classmethod
    def post(cls):
        lead_json = request.get_json()
        lead = leads_schema.load(lead_json)

        if LeadsModel.find_by_email(lead.email):
            return {"message": gettext("lead_email_already_exists")}, 400

        if LeadsModel.find_by_name(lead.first_name):
            return {"message":gettext("lead_name_already_exists")}, 400

        leadId = lead.save_to_db()
        leadName = 'TMP-'+str(leadId)
        LeadArr = LeadsModel.find_by_id(leadId)
        LeadArr.lead_id = leadName
        LeadArr.save_to_db()

        return {"message": gettext("lead_registered") + " "+ leadName}, 201
        
    @classmethod
    def put(cls,leadId):
        leadJson = request.get_json()
        leadRecord = LeadsModel.find_by_id(leadId)
        
        if leadRecord:
            leadRecord.vechile_type = leadJson['vechile_type']
            leadRecord.make = leadJson['make']
            leadRecord.model = leadJson['model']
            leadRecord.vin = leadJson['vin']
        else:
            return {"message": gettext("lead_not_found")}, 401
        
        leadRecord.save_to_db()

        return {"message":gettext("lead_updated_successfully")},200



class Leads(Resource):
    @classmethod
    def get(cls, lead_id: int):
        lead = LeadsModel.find_by_id(lead_id)
        if not lead:
            return {"message": gettext("lead_not_found")}, 404
        print(lead.makeObj.name)
        return leads_schema.dump(lead), 200