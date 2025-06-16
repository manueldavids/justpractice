""" As every other extension, you can initialize it with an application object:"""
from flask import Flask
from flask_restx import Api


app = Flask(__name__)
api = Api(app)

"""or lazily with the factory pattern:"""

from flask import Flask
from flask_restx import Api


api = Api()

app = Flask(__name__)
api.init_app(app)

