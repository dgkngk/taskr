from flask import Flask, g
from flask_restful import Api
from dotenv import load_dotenv
from resources import Index, TaskResource

load_dotenv("./.flaskenv")


app = Flask(__name__)
api = Api(app)

api.add_resource(Index, '/')
api.add_resource(TaskResource, '/task/<string:task_id>')

@app.after_request

def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
  return response
    
if __name__ == "__main__":
    app.run()