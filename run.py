from lib.flask.app import FlaskHandler
from lib.flask.resources.hello_world import HelloWorld
import os

config_name = os.getenv('APP_SETTINGS')

flask = FlaskHandler()
flask.add_resource(HelloWorld,'/')

if __name__ == '__main__':
  flask.app.run(debug=True)

