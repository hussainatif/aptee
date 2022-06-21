#importing required packages
from email import message
import pygsheets
import flask
import pandas as pd
from flask_login import UserMixin
from wtforms import Form,StringField,PasswordField,SubmitField
from wtforms.validators import InputRequired, Length, ValidationError,Email
app = flask.Flask(__name__, template_folder="Templates")
app.config['SECRET_KEY']='abcdefghijkhlmnop'
class SignupForm(Form):
        email_id = StringField(id='Register_email',validators=[InputRequired(), Length(min=4, max=20),Email(message="Come on Bro")],render_kw={"placeholder": "Let the autofill complete it @gmail.com"})
        password = PasswordField(id='Register_password',validators=[InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Type in a password you won't remember"})
        name=StringField(id='Register_name',validators=[InputRequired()],render_kw={"placeholder": "What should we call you?"})
        submit = SubmitField('Register')
@app.route('/', methods =['POST', 'GET'])
def home():
        form = SignupForm(flask.request.form)
        return flask.render_template('index.html',form=form)
@app.route('/Signup', methods =['POST'])
def Signup():
        form =SignupForm(flask.request.form)
        email=form.email_id.data
        gc = pygsheets.authorize(service_file = 'Auth.json')
        sh = gc.open_by_url('https://docs.google.com/spreadsheets/d/1CyWjl6Y5Gi_e3z7A8wtw-qOaBe3GvCD4sqWWvaMubXY/edit?usp=sharing')
        wks = sh.worksheet_by_title('Client_Details')
        df = wks.get_as_df()
        if len(df[df['email_id']==email])>0:
                return flask.render_template('index.html',form=form,message="The Email is already registered Please Login")
        else:
                cells = wks.get_all_values(include_tailing_empty_rows=False, include_tailing_empty=False, returnas='matrix')
                wks = wks.insert_rows(len(cells), number=1, values= [form.email_id.data,form.name.data,'','','','','','','','','',form.password.data])
        return flask.render_template('index.html',form=form)

if __name__ == '__main__':
    app.run(debug = True)