import json
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

ENV = 'dev'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = ''
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = ''

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Database(db.model):
    __tablename__ = 'FormIn'
    id = db.Column(db.Integer, primary_key=true)
    nameCusto = db.Column(db.String(200))
    tgglCusto = db.Column(db.DateTime())
    jeKelamin = db.Column(db.String(200))
    jeIdentit = db.Column(db.String(200))
    noIdentit = db.Column(db.Integer)
    noTelepon = db.Column(db.Integer)
    alamatKtp = db.Column(db.Text())

    def __init__(self, nameCusto, tgglCusto, jeKelamin, jeIdentit, noIdentit, noTelepon, alamatKtp):
        self.nameCusto = nameCusto
        self.tgglCusto = tgglCusto
        self.jeKelamin = jeKelamin
        self.jeIdentit = jeIdentit
        self.noIdentit = noIdentit
        self.noTelepon = noTelepon
        self.alamatKtp = alamatKtp


@app.route('/')
class HelloWorld(Resource):
    def get(self):
        return jsonify({'name': 'Hello',
                    'email': 'Hello World!'})

@app.route('/bambang/masuk', methods=['POST'])
class Bambang(Resource):
    def get(self):
        return {'hello': 'bambang!'}

@app.route('/bambang/masuk', methods=['POST'])
class inGet(Resource):
    def get(self):
        header = ['Nama', 'Tgl', 'JK', 'JI', 'NI', 'NT', 'AK']
        if request.method == 'POST':
            nameCusto = request.form['Nama']
            tgglCusto = request.form['TgglLr']
            jeKelamin = request.form['JKel']
            jeIdentit = request.form['JIden']
            noIdentit = request.form['NoIden']
            noTelepon = request.form['NoTel']
            alamatKtp = request.form['AlamatKTP']
            suhuBadan = request.form['Suhu']
            provTujIn = request.form['provTujIn']
            kebpTujIn = request.form['kebpTujIn']
            kecmTujIn = request.form['kecmTujIn']
            alamTujIn = request.form['alamTujIn']
            provTujOu = request.form['provTujOu']
            kabpTujOu = request.form['kabpTujOu']
            kecmTujOu = request.form['kecmTujOu']
            alamTujOu = request.form['alamTujOu']

            if db.session.query(Database).filter(Database.nameCusto == nameCusto).count() == 0:
                data = Database(nameCusto, tgglCusto, jeKelamin, jeIdentit, noIdentit, noTelepon, alamatKtp)
                db.session.add(data)
                db.session.commit()
                return {
                    "Nama" : nameCusto,
                    "Tanggal" : tgglCusto,
                    "jeKelamin" : jeKelamin,
                    "jeIdentit" : jeIdentit,
                    "noIdentit" : noIdentit,
                    "noTelepon" : noTelepon,
                    "alamatKtp" : alamatKtp
                }
        return {"message": "Data Berhasil ditambahkan"}

@app.route('/bambang/keluar', methods=['POST'])
class outGet(Resource):
    def get(self):
        if request.is_json:
            data = request.get_json()
            return {"message": data}
        else:
            return {"error"}

api.add_resource(HelloWorld, '/')
api.add_resource(inGet, '/bambang/masuk')
api.add_resource(outGet, '/bambang/keluar')
api.add_resource(outGet, '/bambang/recommendation')


if __name__ == '__main__':
     app.run(threaded=True, port=5000)