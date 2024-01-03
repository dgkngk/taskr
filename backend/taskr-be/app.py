from flask import Flask, g
from flask_restful import Api
from dotenv import load_dotenv
from resources import Index, TaskResource
from utils.context_manager import ContextManager

load_dotenv("./.flaskenv")

def get_ctx():
    if not hasattr(g, 'ctx'):
        g.ctx = ContextManager()
    return g.ctx

app = Flask(__name__)
api = Api(app)

api.add_resource(Index, '/')
api.add_resource(TaskResource, '/task/<string:task_id>')
    
if __name__ == "__main__":
    app.run()