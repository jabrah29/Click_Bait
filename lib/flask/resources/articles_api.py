from flask_restful import Resource, reqparse


class ArticlesApi(Resource):

  def post(self):
    parser = reqparse.RequestParser()
    parser.add_argument('title', type=int, help='Rate cannot be converted')
    args = parser.parse_args()
    print(args)
    return args, 201


