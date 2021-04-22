from flask import Flask, jsonify, request
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return jsonify({'Message': 'Semangat Memberantas Covid Bambang Covid!',
                    'email': 'bambangcovid@kenacovid.aw.com'})

@app.route('/form-in',methods=['POST'])
def formIn():
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
        provTujIn = data['provinsi_asal']
        kebpTujIn = data['kabupaten_asal']
        kecmTujIn = data['kecamatan_asal']
        alamTujIn = data['alamat_asal']
        provTujOu = data['provinsi_tujuan']
        kabpTujOu = data['kabupaten_tujuan']
        kecmTujOu = data['kecamatan_tujuan']
        alamTujOu = data['alamat_tujuan']
        return jsonify(data), 200
    except Exception as e:
        return {'error':str(e)}

@app.route('/form-out',methods=['POST'])
def formOut():
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
        provTujIn = data['provinsi_asal']
        kebpTujIn = data['kabupaten_asal']
        kecmTujIn = data['kecamatan_asal']
        alamTujIn = data['alamat_asal']
        provTujOu = data['provinsi_tujuan']
        kabpTujOu = data['kabupaten_tujuan']
        kecmTujOu = data['kecamatan_tujuan']
        alamTujOu = data['alamat_tujuan']
        return jsonify(data), 200
    except Exception as e:
        return {'error':str(e)}

@app.route('/rekomendasi-tempat',methods=['GET','POST'])
def rekomendasitempat():
    if request.method == 'GET':
        try:
            namaTmpt = request.args.get('nama_tempat')
            provinsi = request.args.get('provinsi']
            kabupatn = request.args.get('kabupaten']
            kecamatn = request.args.get('kecamatan']
            alamat = request.args.get('alamat']
            jenis = request.args.get('jenis']
            telepon = request.args.get('telepon']
            ketersed = request.args.get('ketersediaan_ruang']
            return redirect(url_for('success',name = namaTmpt))
        except Exception as e:
            return {'error':str(e)}
    else:
        try:
            data = request.get_json(force=True)
            namaTmpt = data['nama_tempat']
            provinsi = data['provinsi']
            kabupatn = data['kabupaten']
            kecamatn = data['kecamatan']
            alamat = data['alamat']
            jenis = data['jenis']
            telepon = data['telepon']
            ketersed = data['ketersediaan_ruang']
            return jsonify(data), 200
        except Exception as e:
            return {'error':str(e)}
        
api.add_resource(HelloWorld, '/')
#api.add_resource(inGet, '/form-in')
#api.add_resource(outGet, '/form-out')

if __name__ == '__main__':
     app.run(threaded=True, port=5000)