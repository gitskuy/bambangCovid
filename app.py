from flask import Flask, jsonify, request
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return jsonify({'name': 'Hello',
                    'email': 'Hello World!'})

class inGet(Resource):
    def get(self):
        json_data = request.get_json(force=True)
        return {jsonify(json_data)}

class outGet(Resource):
    def get(self):
        json_data = request.get_json(force=True)
        return {jsonify(json_data)}

api.add_resource(HelloWorld, '/')
api.add_resource(inGet, '/form-in')
api.add_resource(outGet, '/form-out')

if __name__ == '__main__':
     app.run(threaded=True, port=5000)