from app import app
from app.form import RegistrationFormIn
from flask import render_template

@app.route("/", methods=['GET','POST'])
@app.route("/form-in", methods=['GET','POST'])
def index():
    form = RegistrationFormIn()
    return render_template('index.html',form=form)