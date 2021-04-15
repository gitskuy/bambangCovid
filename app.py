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
        data = request.get_json(force=True)
        nameCusto = data['Nama']
        tgglCusto = data['TgglLr']
        jeKelamin = data['JKel']
        jeIdentit = data['JIden']
        noIdentit = data['NoIden']
        noTelepon = data['NoTel']
        alamatKtp = data['AlamatKTP']
        suhuBadan = data['Suhu']
        provTujIn = data['provTujIn']
        kebpTujIn = data['kebpTujIn']
        kecmTujIn = data['kecmTujIn']
        alamTujIn = data['alamTujIn']
        provTujOu = data['provTujOu']
        kabpTujOu = data['kabpTujOu']
        kecmTujOu = data['kecmTujOu']
        alamTujOu = data['alamTujOu']
        return {jsonify(json_data)}

class outGet(Resource):
    def get(self):
        if data:
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
            return {jsonify(data)}
        else:
            return{'Message':'Data Tidak Ditemukan atau Gagal Parsing'}

class outGet(Resource):
    def get(self):
        if data:
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
            return {jsonify(data)}
        else:
            return{'Message':'Data Tidak Ditemukan atau Gagal Parsing'}

api.add_resource(HelloWorld, '/')
api.add_resource(inGet, '/form-in')
api.add_resource(outGet, '/form-out')

if __name__ == '__main__':
     app.run(threaded=True, port=5000)