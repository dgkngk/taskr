from flask import Flask
from flask_restful import Api
from dotenv import load_dotenv
from resources import Index, TaskResource

load_dotenv("./.flaskenv")

app = Flask(__name__)
api = Api(app)

api.add_resource(Index, '/')
api.add_resource(TaskResource, '/task/<string:task_id>')
    
if __name__ == "__main__":
    app.run()