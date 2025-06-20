from flask import Flask
from flask_restx import Resource, Api


app = Flask(__name__)
api = Api(app)

class Todo1(Resource):
    def get(self):
        """ Default to 200 OK"""
        return {'task': 'Hello world'}

class Todo2(Resource):
    def get(self):
        """ Set the response code to 201"""
        return {'task': 'Hello world'}, 201, {'Etag': 'some-opaque-strinng'}

class Todo3(Resource):
    def get(self):
        """ Set the response code 201 and the return custom headers """

"""Add the routes"""
api.add_resource(Todo1, '/todo1')
api.add_resource(Todo2, '/todo2')
api.add_resource(Todo3, '/todo3')

if __name__ == '__main__':
    app.run(debug=True)
