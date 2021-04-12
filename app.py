import json
from flask import Flask,jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return jsonify({'name': 'Hello',
                    'email': 'Hello World!'})
    def put(self,user_id):
       
class Bambang(Resource):
    def get(self):
        return {'hello': 'bambang!'}

class inGet(Resource):
    def get(self):
        return {"message": "Data Berhasil ditambahkan"}

class outGet(Resource):
    def get(self):
        return {"message": "Data berhasil ditambahkan"}

api.add_resource(HelloWorld, '/')
api.add_resource(Bambang, '/BambangZ')
api.add_resource(inGet, '/bambang/masuk')
api.add_resource(Bambang, '/bambang/keluar')


if __name__ == '__main__':
     app.run(threaded=True, port=5000)