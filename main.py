import os
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

class Bambang(Resource):
    def get(self):
        return {'hello': 'bambang!'}

api.add_resource(HelloWorld, '/')
api.add_resource(Bambang, '/BambangZ')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)