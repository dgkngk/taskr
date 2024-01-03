from flask_restful import Resource
from utils import ctx


class Index(Resource):
    def get(self):
        return ctx.get_all_tasks()
    
    def post(self):
        return "Taskr Backend API v1.0.0"