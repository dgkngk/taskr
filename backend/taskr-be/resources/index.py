from flask_restful import Resource
from utils import ctx


class Index(Resource):
    def get(self):
        all_tasks = ctx.get_all_tasks()
        res = []
        if all_tasks:
            for task in all_tasks:
                if task.active:
                    res.append(task.as_dict())
            return res
        return "No task is available"
    
    def post(self):
        return "Taskr Backend API v1.0.0"