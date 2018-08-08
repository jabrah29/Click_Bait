from flask import Flask, request

app = Flask(__name__)

mock_data = {
  'test':'hello'
}

@app.route("/titles")
def get_titles():
  return mock_data, 201


@app.route("/titles", methods=['POST'])
def test_title():
  print(request.form['title'])
  return '', 204

