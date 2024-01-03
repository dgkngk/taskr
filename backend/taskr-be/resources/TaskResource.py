from flask_restful import Resource
from utils import ctx
from flask import request
from datamodels.TaskModel import TaskModel


class TaskResource(Resource):
    def get(self, task_id: str):
        if not task_id or task_id == "all" or task_id == "": # all tasks
            return ctx.get_all_tasks()
        else:
            if not ctx.task_exists(task_id):
                return "Not found", 404
            return ctx.get_task(task_id)
    
    def post(self, task_id: str):
        if not task_id:
            return "Bad request", 400
        if ctx.task_exists(task_id): # update
            json = request.get_json()
            if not json:
                return "Bad request json not parsed", 400
            
            task_obj = TaskModel()
            if not task_obj.set_with_dict(json):
                return "Bad request cannot set task", 400
            
            return ctx.update_task(task_id, task_obj)
        else: # create
            json = request.get_json()
            if not json:
                return "Bad request json not parsed", 400
            
            task_obj = TaskModel()
            if not task_obj.set_with_dict(json):
                return "Bad request cannot set task", 400
            return ctx.add_task(task_obj)
    
    def delete(self, task_id: str):
        if not task_id:
            return "Bad request", 400
        if not ctx.task_exists(task_id):
            return "Not found", 404
        return ctx.remove_task(task_id)
    