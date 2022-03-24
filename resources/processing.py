from flask_restful import Resource
from flask import request

class processing(Resource):
    @classmethod
    def post(cls):
        donationData = request.get_json()
        print(donationData)
        return 
