from flask import Flask, request, render_template
import json


app = Flask(__name__)

mock_data = {
  'test':'hello'
}

@app.route("/title", methods=['POST'])
def test_title():
  title = request.args['title']
  return render_template('result.html', value=title)
