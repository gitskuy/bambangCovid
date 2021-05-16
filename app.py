from flask import Flask, jsonify, request
from flask_restful import reqparse, abort, Api, Resource
from flask_sqlalchemy import SQLAlchemy
import psycopg2
import datetime


app = Flask(__name__)

db_host = "ec2-34-225-103-117.compute-1.amazonaws.com"
db_name = "d1ati88i3hiodn"
db_user = "vputlrxzjcwffs"
db_pass = "ebc3f1ac8d6de628c643fe9440f03ffe691918d34784868f807d31cf1da09efd"

connection = psycopg2.connect(dbname=db_name, user=db_user, password=db_pass, host=db_host)
cursor = connection.cursor()

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://vputlrxzjcwffs:ebc3f1ac8d6de628c643fe9440f03ffe691918d34784868f807d31cf1da09efd@ec2-34-225-103-117.compute-1.amazonaws.com:5432/d1ati88i3hiodn'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api = Api(app)

db=SQLAlchemy(app)

dateX = datetime.datetime.now()

class login(db.Model):
    __tablename__='Login'

    username = db.Column(db.String, primary_key=True)
    password = db.Column(db.String)

    def __init__(self, username, password):
        self.username = username
        self.password = password

class rekTempat(db.Model):
    __tablename__='RekTempat'

    namaTmpt = db.Column(db.String, primary_key=True)
    provinsi = db.Column(db.Text())
    kabupatn = db.Column(db.Text())
    kecamatn = db.Column(db.Text())
    alamat = db.Column(db.Text())
    jenis = db.Column(db.Text())
    telepon = db.Column(db.Integer) 
    ketersed = db.Column(db.Integer) 

    def __init__(self, namaTmpt, provinsi, kabupatn, kecamatn, alamat, jenis, telepon, ketersed):
        self.namaTmpt = namaTmpt
        self.provinsi = provinsi
        self.kabupatn = kabuptn
        self.kecamatn = kecamatn
        self.alamat = alamat
        self.jenis = jenis
        self.telepon = telepon
        self.ketersed = ketersed

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
    tangMskIn = db.Column(db.String)
    statusPer = db.Column(db.String)
    karanName = db.Column(db.Text())    

    def __init__(self, nameCusto, tgglCusto, jeKelamin, jeIdentit, noIdentit, noTelepon, alamatKtp, suhuBadan, dftrGjala, gjalalain, kontatsta, provTujIn, kebpTujIn, kecmTujIn, alamTujIn, provTujOu, kabpTujOu, kecmTujOu, alamTujOu, tangMskIn, statusPer, karanName):
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
        self.tangMskIn = tangMskIn
        self.statusPer = statusPer
        self.karanName = karanName

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
    tangMskOu = db.Column(db.String)
    statusPer = db.Column(db.String)
    karanName = db.Column(db.Text())

    def __init__(self, nameCusto, tgglCusto, jeKelamin, jeIdentit, noIdentit, noTelepon, alamatKtp, suhuBadan, dftrGjala, gjalalain, kontatsta, provTujIn, kebpTujIn, kecmTujIn, alamTujIn, provTujOu, kabpTujOu, kecmTujOu, alamTujOu, tangMskOu, statusPer, karanName):
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
        self.tangMskOu = tangMskOu
        self.statusPer = statusPer
        self.karanName = karanName

class HelloWorld(Resource):
    def get(self):
        return jsonify({'Message': 'Semangat Memberantas Covid Bambang Covid!',
                    'email': 'bambangcovid@kenacovid.aw.com'})

@app.route('/login', methods = ["GET", "POST"])
def login():
    if request.method == "POST":  
        data = request.get_json()
        nameCusto = data['un']
        tgglCusto = data['pw']
        if nameCusto=="admin" and tgglCusto=="adminmantap":
            return{'Message':'Login Sukses'}
        if nameCusto=="adminteam" and tgglCusto=="adminmantap":
            return{'Message':'Login Sukses'}
        else:
            return{'Message':'Login Gagal'}

@app.route('/logout', methods = ["POST"])
def logout():
    return {'Message':'Logout Sukses'}

@app.route("/edit-rekomendasi", methods=['GET','POST'])
def editRekomendasi():
    data = request.get_json()
    namaTmpt = data['nama_tempat']
    provinsi = data['provinsi']
    kabupatn = data['kabupaten']
    kecamatn = data['kecamatan']
    alamat = data['alamat']
    jenis = data['jenis']
    telepon = data['telepon']
    ketersed = data['ketersediaan_ruang']

    try:
        newtitle = request.form.get("newtitle")
        oldtitle = request.form.get("oldtitle")
        book = Book.query.filter_by(title=oldtitle).first()
        book.title = newtitle
        db.session.commit()
    except Error as error:
        return {"Message": 'Error gan'}

@app.route("/search", methods=['GET','POST'])
def searchOut():  
    data = request.get_json()
    t_input = data['nomor_identitas']
    print(t_input)
    s = 'SELECT * FROM public."UserIn" WHERE "noIdentit" LIKE ' 
    s += "'%t_input%'"
    s += "UNION ALL"
    s += 'SELECT * FROM public."UserOut" WHERE "noIdentit" LIKE '
    s += "'%t_input%'"
    try:
        cursor.execute(s, (tuple(t_input)))
        dbRow = cursor.fetchall()
    except psycopg2.Error as e:
        t_message = "Postgres Database error: " + e + "/n SQL: " + s
        return {"Massage":t_input}
    cursor.close

@app.route('/form-in',methods=['GET', 'POST'])
def formIn():
    if request.method == "POST":
        try:
            data = request.get_json()
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
                statusPer = 'Karantina'
            else:
                statusPer = 'Tidak Karantina'
            kontatsta = data['is_kontak_positif']
            provTujIn = data['provinsi_asal']
            kebpTujIn = data['kabupaten_asal']
            kecmTujIn = data['kecamatan_asal']
            alamTujIn = data['alamat_asal']
            provTujOu = data['provinsi_tujuan']
            kabpTujOu = data['kabupaten_tujuan']
            kecmTujOu = data['kecamatan_tujuan']
            alamTujOu = data['alamat_tujuan']
            tangMskIn = dateX.strftime("%d-%m-%Y")
            karanName = data['rekomendasi_karantina']
            if nameCusto == '':
                return {'Message':'Data Tidak Ada'}
            else:
                db_data = UserIn(nameCusto, tgglCusto, jeKelamin, jeIdentit, noIdentit, noTelepon, alamatKtp, suhuBadan, dftrGjala, gjalalain, kontatsta, provTujIn, kebpTujIn, kecmTujIn, alamTujIn, provTujOu, kabpTujOu, kecmTujOu, alamTujOu, tangMskIn, statusPer, karanName)
                db.session.add(db_data)
                db.session.commit()
            return jsonify(data), 200
        except Exception as e:
            return {'error':str(e)}
    else:
        try:
            data = UserIn.query.order_by(UserIn.tgglCusto).all()
            print(type(data))
            dataJson = []
            for i in range(len(data)):
                dataDict = {
                    'nama_lengkap': str(data[i].nameCusto),
                    'tanggal_lahir': str(data[i].tgglCusto),
                    'jenis_kelamin': str(data[i].jeKelamin),
                    'jenis_identitas': str(data[i].jeIdentit),
                    'nomor_identitas': str(data[i].noIdentit),
                    'no_telepon': str(data[i].noTelepon),
                    'alamat_sesuai_ktp': str(data[i].alamatKtp),
                    'suhu_badan': str(data[i].suhuBadan),
                    'tidak_ada_gejala': str(data[i].noTelepon),
                    'daftar_gejala': str(data[i].dftrGjala),
                    'gejala_lain': str(data[i].gjalalain),
                    'is_kontak_positif': str(data[i].kontatsta),
                    'provinsi_asal': str(data[i].provTujIn),
                    'kabupaten_asal': str(data[i].kebpTujIn),
                    'kecamatan_asal': str(data[i].kecmTujIn),
                    'alamat_asal': str(data[i].alamTujIn),
                    'provinsi_tujuan': str(data[i].provTujOu),
                    'kabupaten_tujuan': str(data[i].kabpTujOu),
                    'kecamatan_tujuan': str(data[i].kecmTujOu),
                    'alamat_tujuan': str(data[i].alamTujOu),
                    'tanggal_masuk': str(data[i].tangMskIn),
                    'status_person': str(data[i].statusPer),
                    'rekomendasi_karantina': str(data[i].karanName)
                }
                dataJson.append(dataDict)
            return jsonify(dataJson)
        except Exception as e:
            return {'error':str(e)}


@app.route('/form-out',methods=['GET','POST'])
def formOut():
    if request.method == "POST":
        try:
            data = request.get_json()
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
                statusPer = 'Karantina'
            else:
                statusPer = 'Tidak Karantina'
            kontatsta = data['is_kontak_positif']
            provTujIn = data['provinsi_asal']
            kebpTujIn = data['kabupaten_asal']
            kecmTujIn = data['kecamatan_asal']
            alamTujIn = data['alamat_asal']
            provTujOu = data['provinsi_tujuan']
            kabpTujOu = data['kabupaten_tujuan']
            kecmTujOu = data['kecamatan_tujuan']
            alamTujOu = data['alamat_tujuan']
            tangMskOu = dateX.strftime("%d-%m-%Y")
            karanName = data['rekomendasi_karantina']
            if nameCusto == '':
                return {'Message':'Data Tidak Ada'}
            else:
                data = UserOut(nameCusto, tgglCusto, jeKelamin, jeIdentit, noIdentit, noTelepon, alamatKtp, suhuBadan, dftrGjala, gjalalain, kontatsta, provTujIn, kebpTujIn, kecmTujIn, alamTujIn, provTujOu, kabpTujOu, kecmTujOu, alamTujOu, tangMskOu, statusPer, karanName)
                db.session.add(data)
                db.session.commit()
                print(data)
            return jsonify(data), 200
        except Exception as e:
            return {'error':str(e)}
    else:
        try:
            data = UserOut.query.order_by(UserOut.tgglCusto).all()
            dataJson = []
            for i in range(len(data)):
                dataDict = {
                    'nama_lengkap': str(data[i].nameCusto),
                    'tanggal_lahir': str(data[i].tgglCusto),
                    'jenis_kelamin': str(data[i].jeKelamin),
                    'jenis_identitas': str(data[i].jeIdentit),
                    'nomor_identitas': str(data[i].noIdentit),
                    'no_telepon': str(data[i].noTelepon),
                    'alamat_sesuai_ktp': str(data[i].alamatKtp),
                    'suhu_badan': str(data[i].suhuBadan),
                    'tidak_ada_gejala': str(data[i].noTelepon),
                    'daftar_gejala': str(data[i].dftrGjala),
                    'gejala_lain': str(data[i].gjalalain),
                    'is_kontak_positif': str(data[i].kontatsta),
                    'provinsi_asal': str(data[i].provTujIn),
                    'kabupaten_asal': str(data[i].kebpTujIn),
                    'kecamatan_asal': str(data[i].kecmTujIn),
                    'alamat_asal': str(data[i].alamTujIn),
                    'provinsi_tujuan': str(data[i].provTujOu),
                    'kabupaten_tujuan': str(data[i].kabpTujOu),
                    'kecamatan_tujuan': str(data[i].kecmTujOu),
                    'alamat_tujuan': str(data[i].alamTujOu),
                    'tanggal_keluar': str(data[i].tangMskOu),
                    'status_person': str(data[i].statusPer),
                    'rekomendasi_karantina': str(data[i].karanName)
                }
                dataJson.append(dataDict)
            return jsonify(dataJson)
        except Exception as e:
            return {'error':str(e)}

@app.route('/rekomendasi-tempat',methods=['GET','POST'])
def rekomendasitempat():
    if request.method == 'GET':
        try:
            data = rekTempat.query.order_by(rekTempat.namaTmpt).all()
            dataJson = []
            for i in range(len(data)):
                dataDict = {
                    'nama_tempat': str(data[i].namaTmpt),
                    'provinsi': str(data[i].provinsi),
                    'kabupaten': str(data[i].kabupatn),
                    'kecamatan': str(data[i].kecamatn),
                    'alamat': str(data[i].alamat),
                    'jenis': str(data[i].jenis),
                    'telepon': str(data[i].telepon),
                    'ketersediaan_ruang': str(data[i].ketersed)
                }
                dataJson.append(dataDict)
            return jsonify(dataJson)
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
