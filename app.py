from flask import Flask, jsonify, request
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)



class HelloWorld(Resource):
    def get(self):
        return jsonify({'Message': 'Semangat Memberantas Covid Bambang Covid!',
                    'email': 'bambangcovid@kenacovid.aw.com'})

@app.route('/form',methods=['POST'])
def coba():
    data = request.get_json(force=True)
    return data['nama_lengkap']

class inGet(Resource):
    def get(self):
        try:
            data = request.get_json(force=True)
            nameCusto = data['nama_lengkap']
            tgglCusto = data['tanggal_lahir']
            jeKelamin = data['jenis_kelamin']
            jeIdentit = data['jenis_identitas']
            noIdentit = data['nomor_identitas']
            noTelepon = data['no_telepon']
            alamatKtp = data['alamat_sesuai_ktp']
            suhuBadan = data['suhu_badan']
            if data['tidak_ada_gejala'] == False:
                dftrGjala = data['daftar_gejala']
                gjalalain = data['gejala_lain']
            else:
                pass
            kontatsta = data['is_kontak_positif']
            provTujIn = data['provTujIn']
            kebpTujIn = data['kebpTujIn']
            kecmTujIn = data['kecmTujIn']
            alamTujIn = data['alamTujIn']
            provTujOu = data['provTujOu']
            kabpTujOu = data['kabpTujOu']
            kecmTujOu = data['kecmTujOu']
            alamTujOu = data['alamTujOu']
            return jsonify(data), 200
        except Exception as e:
            return {'error':str(e)}

class outGet(Resource):
    def get(self):
        try:
            data = request.get_json(force=True)
            nameCusto = data['nama_lengkap']
            tgglCusto = data['tanggal_lahir']
            jeKelamin = data['jenis_kelamin']
            jeIdentit = data['jenis_identitas']
            noIdentit = data['nomor_identitas']
            noTelepon = data['no_telepon']
            alamatKtp = data['alamat_sesuai_ktp']
            suhuBadan = data['suhu_badan']
            if data['tidak_ada_gejala'] == True:
                dftrGjala = data['daftar_gejala']
                gjalalain = data['gejala_lain']
            else:
                pass
            kontatsta = data['is_kontak_positif']
            provTujIn = data['provTujIn']
            kebpTujIn = data['kebpTujIn']
            kecmTujIn = data['kecmTujIn']
            alamTujIn = data['alamTujIn']
            provTujOu = data['provTujOu']
            kabpTujOu = data['kabpTujOu']
            kecmTujOu = data['kecmTujOu']
            alamTujOu = data['alamTujOu']
            return jsonify(data), 200
        except Exception as e:
            return {'error':str(e)}
        

api.add_resource(HelloWorld, '/')
api.add_resource(inGet, '/form-in')
api.add_resource(outGet, '/form-out')

if __name__ == '__main__':
     app.run(threaded=True, port=5000)