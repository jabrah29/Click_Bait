from flask import Flask, jsonify, request

app = Flask(__name__)

mock_data = {
  'test':'hello'
}

@app.route("/titles")
def get_titles():
  return mock_data, 201


@app.route("/titles", methods=['POST'])
def test_title():
  print(request.get_json())

