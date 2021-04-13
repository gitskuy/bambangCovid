from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField, IntegerField, DateField, SelectField
from wtforms.fields.html5 import TelField
from wtforms.validators import DataRequired, ValidationError

class RegistrationFormIn(FlaskForm):
    name = StringField('Nama Lengkap', validators = [DataRequired()])
    dateBorn = DateField('Tanggal Lahir', format='%m/%d/%Y')
    jKelamin = StringField('Jenis Kelamin', validators = [DataRequired()])
    jIdentitas = StringField('Jenis Identitas', validators = [DataRequired()])
    noIdentitas = IntegerField('Nomor Identitas', validators = [DataRequired()])
    noTelepon = TelField('Nomor Telepon', validators = [DataRequired()])
    alamat = StringField('Alamat', validators = [DataRequired()])
    submit = SubmitField('')

    suhu = IntegerField('Suhu Badan', validators = [DataRequired()])
    op0 = request.form.getlist('Demam')
    op1 = request.form.getlist('Batuk Kering')
    op2 = request.form.getlist('Pilek')
    op3 = request.form.getlist('Sesak Nafas')
    op4 = request.form.getlist('Pegal-pegal')
    op5 = request.form.getlist('Lemas/Letih')
    op6 = request.form.getlist('Sakit Kepala')
    op7 = request.form.getlist('Tidak Ada Gejala')

    otherAsymp = StringField('Gejala Lainnya')
    poll_data = {
        'question' : 'Apakah anda melakukan kontak dengan pasien covid-19 dalam 14 hari terakhir?'
        'fields' : ['Ya','Tidak']
        }
    
    submit = SubmitField('')



    'provinsi tujuan'
    'Kabupaten Tujuan'
    'Kecamatan Tujuan'
    'Alamat tujuan'
    submit = SubmitField('')

    'provinsi Asal'
    'Kabupaten Asal'
    'Kecamatan Asal'
    'Alamat Asal'
    submit = SubmitField('')