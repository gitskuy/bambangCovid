from flask import Flask, jsonify, request
from flask_restful import reqparse, abort, Api, Resource
from flask_sqlalchemy import SQLAlchemy
import psycopg2


app = Flask(__name__)

db_host = "ec2-34-225-103-117.compute-1.amazonaws.com"
db_name = "d1ati88i3hiodn"
db_user = "vputlrxzjcwffs"
db_pass = "ebc3f1ac8d6de628c643fe9440f03ffe691918d34784868f807d31cf1da09efd"

connection = psycopg2.connect(dbname=db_name, user=db_user, password=db_pass, host=db_host)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://vputlrxzjcwffs:ebc3f1ac8d6de628c643fe9440f03ffe691918d34784868f807d31cf1da09efd@ec2-34-225-103-117.compute-1.amazonaws.com:5432/d1ati88i3hiodn'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api = Api(app)

db=SQLAlchemy(app)

class UserIn(db.Model):
    __tablename__='UserIn'

    nameCusto = db.Column(db.String, primary_key=True)
    tgglCusto = db.Column(db.String)
    jeKelamin = db.Column(db.String)
    jeIdentit = db.Column(db.String)
    noIdentit = db.Column(db.String)
    noTelepon = db.Column(db.String)
    alamatKtp = db.Column(db.String)
    suhuBadan = db.Column(db.Integer) 
    dftrGjala = db.Column(db.Text())
    gjalalain = db.Column(db.Text())
    kontatsta = db.Column(db.String)
    provTujIn = db.Column(db.String)
    kebpTujIn = db.Column(db.String)
    kecmTujIn = db.Column(db.String)
    alamTujIn = db.Column(db.String)
    provTujOu = db.Column(db.String)
    kabpTujOu = db.Column(db.String)
    kecmTujOu = db.Column(db.String)
    alamTujOu = db.Column(db.String)

    def __init__(self, nameCusto, tgglCusto, jeKelamin, jeIdentit, noIdentit, noTelepon, alamatKtp, suhuBadan, dftrGjala, gjalalain, kontatsta, provTujIn, kebpTujIn, kecmTujIn, alamTujIn, provTujOu, kabpTujOu, kecmTujOu, alamTujOu):
        self.nameCusto = nameCusto
        self.tgglCusto = tgglCusto
        self.jeKelamin = jeKelamin
        self.jeIdentit = jeIdentit
        self.noIdentit = noIdentit
        self.noTelepon = noTelepon
        self.alamatKtp = alamatKtp
        self.suhuBadan = suhuBadan
        self.dftrGjala = dftrGjala
        self.gjalalain = gjalalain
        self.kontatsta = kontatsta
        self.provTujIn = provTujIn
        self.kebpTujIn = kebpTujIn
        self.kecmTujIn = kecmTujIn
        self.alamTujIn = alamTujIn
        self.provTujOu = provTujOu
        self.kabpTujOu = kabpTujOu
        self.kecmTujOu = kecmTujOu
        self.alamTujOu = alamTujOu

class UserOut(db.Model):
    __tablename__='UserOut'

    nameCusto = db.Column(db.String, primary_key=True)
    tgglCusto = db.Column(db.String)
    jeKelamin = db.Column(db.String)
    jeIdentit = db.Column(db.String)
    noIdentit = db.Column(db.String)
    noTelepon = db.Column(db.String)
    alamatKtp = db.Column(db.String)
    suhuBadan = db.Column(db.Integer) 
    dftrGjala = db.Column(db.Text())
    gjalalain = db.Column(db.Text())
    kontatsta = db.Column(db.String)
    provTujIn = db.Column(db.String)
    kebpTujIn = db.Column(db.String)
    kecmTujIn = db.Column(db.String)
    alamTujIn = db.Column(db.String)
    provTujOu = db.Column(db.String)
    kabpTujOu = db.Column(db.String)
    kecmTujOu = db.Column(db.String)
    alamTujOu = db.Column(db.String)

    def __init__(self, nameCusto, tgglCusto, jeKelamin, jeIdentit, noIdentit, noTelepon, alamatKtp, suhuBadan, dftrGjala, gjalalain, kontatsta, provTujIn, kebpTujIn, kecmTujIn, alamTujIn, provTujOu, kabpTujOu, kecmTujOu, alamTujOu):
        self.nameCusto = nameCusto
        self.tgglCusto = tgglCusto
        self.jeKelamin = jeKelamin
        self.jeIdentit = jeIdentit
        self.noIdentit = noIdentit
        self.noTelepon = noTelepon
        self.alamatKtp = alamatKtp
        self.suhuBadan = suhuBadan
        self.dftrGjala = dftrGjala
        self.gjalalain = gjalalain
        self.kontatsta = kontatsta
        self.provTujIn = provTujIn
        self.kebpTujIn = kebpTujIn
        self.kecmTujIn = kecmTujIn
        self.alamTujIn = alamTujIn
        self.provTujOu = provTujOu
        self.kabpTujOu = kabpTujOu
        self.kecmTujOu = kecmTujOu
        self.alamTujOu = alamTujOu


class HelloWorld(Resource):
    def get(self):
        return jsonify({'Message': 'Semangat Memberantas Covid Bambang Covid!',
                    'email': 'bambangcovid@kenacovid.aw.com'})

@app.route('/login', methods = ["POST"])
def login():
    un = request.form['Username']
    pw = request.form['Password']

    cursor = connection.cursor()
    query1 = "SELECT Username, Password From Users WHERE Username = {un} AND Password = {pw}".format(un = UN, pw = PW)

    rows = cursor.excecute(query1)
    rows = rows.fetchall()
    if len(rows) == 1:
        return('Message':'Login Sukses')
    else:
        return('Message':'Login Gagal')

@app.route('/logout', methods = ["POST"])
def logout():
    return ('Message':'Logout Sukses')


@app.route("/search-in", methods=['GET','POST'])
def searchIn():
    if request.method == "POST":  
        noIden = request.form['noIdentit']
        try:
            cursor.execute("",(noIden))
        except Exception,e:
            conn.rollback()
        else:
            conn.commit()
        data = cursor.fetchall()
        return ("Message":"Data Ditemukan")
    return ("Message":"Data Tidak Ditemukan")

@app.route("/edit-rekomendasi", methods=['GET','POST'])
def editRekomendasi():
    if request.method == "GET":  
        namaTmpt = request.args.get('nama_tempat')
        provinsi = request.args.get('provinsi')
        kabupatn = request.args.get('kabupaten')
        kecamatn = request.args.get('kecamatan')
        alamat = request.args.get('alamat')
        jenis = request.args.get('jenis')
        telepon = request.args.get('telepon')
        ketersed = request.args.get('ketersediaan_ruang')
        

        data = (namaTmpt, provinsi, kabupatn, kecamatn, alamat, jenis, telepon, ketersed)
        try:
            conn = .... 
            cursor = conn.cursor()
            cursor.execute(ini quernya apa.... , data)
            # accept the changes
            conn.commit()

        except Error as error:
            print(error)

        finally:
            cursor.close()
            conn.close()
        return ("Message":"Data Di Update")
    return ("Message":"Error")


@app.route("/search-out", methods=['GET','POST'])
def searchOut():
    if request.method == "POST":  
        noIden = request.form['noIdentit']
        try:
            cursor.execute("",(noIden))
        except Exception,e:
            conn.rollback()
        else:
            conn.commit()
        data = cursor.fetchall()
        return ("Message":"Data Ditemukan")
    return ("Message":"Data Tidak Ditemukan")

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
        if nameCusto == '':
            return {'Message':'Data Tidak Ada'}
        else:
            data = UserIn(nameCusto, tgglCusto, jeKelamin, jeIdentit, noIdentit, noTelepon, alamatKtp, suhuBadan, dftrGjala, gjalalain, kontatsta, provTujIn, kebpTujIn, kecmTujIn, alamTujIn, provTujOu, kabpTujOu, kecmTujOu, alamTujOu)
            db.session.add(data)
            db.session.commit()
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
        if nameCusto == '':
            return {'Message':'Data Tidak Ada'}
        else:
            data = UserOut(nameCusto, tgglCusto, jeKelamin, jeIdentit, noIdentit, noTelepon, alamatKtp, suhuBadan, dftrGjala, gjalalain, kontatsta, provTujIn, kebpTujIn, kecmTujIn, alamTujIn, provTujOu, kabpTujOu, kecmTujOu, alamTujOu)
            db.session.add(data)
            db.session.commit()
        return jsonify(data), 200
    except Exception as e:
        return {'error':str(e)}

@app.route('/rekomendasi-tempat',methods=['GET','POST'])
def rekomendasitempat():
    if request.method == 'GET':
        try:
            namaTmpt = request.args.get('nama_tempat')
            provinsi = request.args.get('provinsi')
            kabupatn = request.args.get('kabupaten')
            kecamatn = request.args.get('kecamatan')
            alamat = request.args.get('alamat')
            jenis = request.args.get('jenis')
            telepon = request.args.get('telepon')
            ketersed = request.args.get('ketersediaan_ruang')
            return {'Message':'Success'}
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