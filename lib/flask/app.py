from flask import Flask
from flask_restful import Resource, Api

class FlaskHandler(object):
  def __init__(self):
    self.app = Flask(__name__)
    self.api = Api(self.app)

  def add_resource(self, resource, route):
    self.api.add_resource(resource, route)
