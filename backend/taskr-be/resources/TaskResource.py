from flask_restful import Resource


class TaskResource(Resource):
    def get(self, task_id: str):
        return f"get {task_id}"
    
    def post(self, task_id: str):
        return f"post {task_id}"
    
    def delete(self, task_id: str):
        return f"delete {task_id}"
    