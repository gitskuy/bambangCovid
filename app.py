import json
from flask import Flask,jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return jsonify({'name': 'Hello',
                    'email': 'Hello World!'})

class Bambang(Resource):
    def get(self):
        return {'hello': 'bambang!'}


api.add_resource(HelloWorld, '/')
api.add_resource(Bambang, '/BambangZ')

if __name__ == '__main__':
     app.run(threaded=True, port=5000)