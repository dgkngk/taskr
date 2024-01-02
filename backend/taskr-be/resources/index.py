from flask_restful import Resource


class Index(Resource):
    def get(self):
        return "Taskr Backend API v1.0.0"