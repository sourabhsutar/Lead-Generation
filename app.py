import imp
from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt_extended import JWTManager
from marshmallow import ValidationError
from dotenv import load_dotenv
from flask_migrate import Migrate

from db import db
from ma import ma
from blacklist import BLACKLIST
from resources.user import UserRegister, UserLogin, User, TokenRefresh, UserLogout
from resources.item import Item, ItemList
from resources.store import Store, StoreList
from resources.order import Order
from resources.leads import Leads, LeadsRegister
from resources.vechicle import Vechicle,VechicleList
from resources.make import Make,MakeList
from resources.model import Model,ModelList
from resources.formatedDate import formatedDate
from resources.processing import processing

app = Flask(__name__)
load_dotenv(".env")
app.config.from_object("default_config")
app.config.from_envvar("APPLICATION_SETTINGS")
api = Api(app)
migrate = Migrate(app,db)


@app.before_first_request
def create_tables():
    db.create_all()


@app.errorhandler(ValidationError)
def handle_marshmallow_validation(err):
    return jsonify(err.messages), 400


jwt = JWTManager(app)


# This method will check if a token is blacklisted, and will be called automatically when blacklist is enabled
def check_if_token_in_blacklist(decrypted_token):
    return decrypted_token["jti"] in BLACKLIST


api.add_resource(Store, "/store/<string:name>")
api.add_resource(StoreList, "/stores")
api.add_resource(Item, "/item/<string:name>")
api.add_resource(ItemList, "/items")
api.add_resource(UserRegister, "/register")
api.add_resource(User, "/user/<int:user_id>")
api.add_resource(UserLogin, "/login")
api.add_resource(TokenRefresh, "/refresh")
api.add_resource(UserLogout, "/logout")
api.add_resource(Order, "/order")
api.add_resource(LeadsRegister,"/leadregister")
api.add_resource(Leads,"/lead/<int:lead_id>")
api.add_resource(Vechicle, "/vechicle/<string:name>")
api.add_resource(VechicleList, "/vechicles")
api.add_resource(Make, "/make")
api.add_resource(MakeList, "/makes")
api.add_resource(Model, "/model")
api.add_resource(ModelList, "/models")
api.add_resource(formatedDate, "/formatedDate/<int:format_id>/<int:interval>")
api.add_resource(processing, "/processing")


if __name__ == "__main__":
    db.init_app(app)
    ma.init_app(app)
    app.run(port=5000, debug=True)
