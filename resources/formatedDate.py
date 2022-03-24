import datetime
from time import strftime
from flask_restful import Resource
from libs.strings import gettext
from datetime import datetime as d,timedelta

class formatedDate(Resource):
    dateformat = {1:'%m/%d/%y',2:'%b %d,%Y',3:'%m-%d-%Y'}
    @classmethod
    def get(cls, format_id:int,interval:int = 0):
        now = d.now()
        end_date = d.now()
        if(format_id in cls.dateformat):
            now = now.strftime(cls.dateformat[format_id])
            end_date = (d.now() + datetime.timedelta(days=interval)).strftime(cls.dateformat[format_id])

        return {'start_date':str(now),'end_date':str(end_date)}, 202