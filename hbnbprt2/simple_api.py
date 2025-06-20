from flask import Flask
from flask_restx import Resource, Api

""" Cerate a Flask app """
app = Flask(__name__)
api = Api(app)

""" Define a simple resource """
@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'message': 'Hello, World!'}

if __name__ == '__main__':
    app.run(debug=True)

