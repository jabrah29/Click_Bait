from flask_restful import Resource

class HelloWorld(Resource):
  def get(self):
    return {"data": "test"}, 201
