#importing required packages
from datetime import datetime
from email import message
import gspread
import flask
from wtforms import Form,StringField,PasswordField,IntegerField,SelectField,EmailField,DateField
from wtforms.validators import InputRequired, Length
import time
import random

app = flask.Flask(__name__, template_folder="Templates")
app.config['SECRET_KEY']='abcdefghijkhlmnop'
#class for signup form
class SignupForm(Form):
        exam=[('CAT','Common Aptitude Test'),('GATE','GATE'),('JOB','Job Aptitude'),('OTH','Others')]
        genders=[('MALE',"Male"),('FEMALE','Female'),('OTHERS','Others')]
        courses=[('Btech','Bachelor of Technology'),('BA','Bachelor of Arts'),('BSc','Bachelor of Science'),('BBA','Bachelor of Business Administration'),
        ('MBA','Master of Business Administration'),('MA','Master of Arts'),('MSc','Master of Science'),('MTech','Master of Technology'),('OTH','Others')]
        email_id = EmailField(id='Register_email',validators=[InputRequired(), Length(min=4, max=20)],render_kw={"placeholder": "Let the autofill complete it @gmail.com"})
        password = PasswordField(id='Register_password',validators=[InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Type in a password you won't remember"})
        name=StringField(id='Register_name',validators=[InputRequired()],render_kw={"placeholder": "What should we call you?"})
        target=SelectField(id='Register_target',validators=[InputRequired()],choices=exam,render_kw={"placeholder": "What is your aim?"})
        gender=SelectField(id='Register_gender',validators=[InputRequired()],choices=genders,render_kw={"placeholder": "What do you identify as?"})
        college=StringField(id='Register_college',validators=[InputRequired()],render_kw={"placeholder": "Where do you study?"})
        college_location=StringField(id='Register_clg_location',validators=[InputRequired()],render_kw={"placeholder": "Where is your college?"})
        course=SelectField(id='Register_course',validators=[InputRequired()],choices=courses,render_kw={"placeholder": "What Course are you enrolled in?"})
        DOB=DateField(id='Register_passout_year',validators=[InputRequired()],render_kw={"placeholder": "Tell us when to wish you?"},format="%Y-%m-%d")
        semester=IntegerField(id='Register_age',validators=[InputRequired()],render_kw={"placeholder": "Which semester are you in? (0 if already passedout) "})
#connecting the login sheet to backend
auth =  {
  "type": "service_account",
  "project_id": "aptee-353914",
  "private_key_id": "0f8783325d8b4b8400bf9f89a6d4b91c1317faf7",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDW4TKM/wixM2BY\nFKQOXExwbNuChLFCjAJuP0MOFfirMISDlxK/HPaKd5iYg9uu/0IG4bC/vO/SzXae\nJXetb3yh3L0KFc4DeAq7fwW2BpJFSAY82ErOTcF6Rfxdq/JrQkXF1WRwHhikrdJy\nDEVfI2Xh2evaeesdLM7/CUPf71LHPrxD14cEsAgAVyIflzADnJagOCKxBNLvhIVL\n5mcXLhDbRiXAFxw2bq10VPI4Bu2dBYJJLXXcU1LV5Jn45Gj4PTYVq//OmOnbxUsU\nNCwgTfMFtgbtOsiULCjq1Zsb7d5YD8Csb/EDSnPqcGUo/dkjyd6nsovz6MDM7Ubo\nn+3/udMpAgMBAAECggEAC6j6MYD4U4dGa9ko4tea1UHu8mjpZoNK8XkQ1i+WiBGQ\nq0RUIdc8QJzHRMVo8xjKWC3AhdMGj4GTNXcyhJCHapAcGPNAc9s8d9qncG5wWv6S\nyhPxkTrSbCRmkp2tQKk+uILBGb1kWHFPOV2VmRlGYshMvlT9z146WEgELR9jNkkF\naOOIb7ZJHlCDOO63R6d04YO2HCmQbRXCPVQrw/CA3k2QCuiSNWCjn68evNQ5KEAl\n07I++ZeaMJzlExePD9BRlqX6lLqD+nLDyng69+QdqcHgMt/gQxgHxMEke3LrqKtO\n7p/S37/RYlJWj2KNY+6lnGzGyXv638exzv9hKGh7FQKBgQD/1DZ7m6N87KRP8WaE\nN9h9zH5EKnZxkBt77LdNWR0TjSE37TCls/SH88fUy0yL/9ZsJe/aHQWG0S7j8yHH\nBWId2xKoFfZUrYMv8csN+CAfDcwPas4Uz8wIvjsdXyfGuOOwtPL22l5NbT1J7TM5\np8kny4bkuif5eknv9IB/320pBQKBgQDXBfnQ2aMT/Kvs+yyttoNccSJ5TfHXL1is\nJMq1miBDqt3635RfXrFufZmqBFVQZKvHTmiymLIknhsSXQicIIDnPq3qBImNf7Fc\nbUGn7eZ8bLVUjSCMm+FeS6v8FYoaK7oejHsNOxpkR2j/EizvmxkYrwseSiDtD4rN\n17FaPMKK1QKBgQCQo62uEx/K2IxJuoUoid53uW9GIO/YYw528S3tqE19KVS3pv3T\nIbxGRTkdAVgk6x+TA5vpKHFgeNJXBLZ7LHr9wEd7Cve7hmJecAlKu5eFlyphKRSc\nxaNo6gzIHW2CuDPbS2L22B1rDzEQo/BLT6a2PiblGK7TKSW2aflg0rSH9QKBgEUd\nzKFPc9YW4AS68C+efTcXvqcTYOt0cqJS6T3anwhhQh1EBONrAsmrYdt+rRW8ZmMY\nVxshbhHLKJSMhxn4cLbkNO8GKljrdM1q6THbjLzuDJNzEcVgzd6LoGrVWaDz8U2k\nhmFIYEFfmuZypzMVvclrar1/wnmxB0MHVCDXawlJAoGBAOxOvLE5Dlm6cxPlGmGb\njam7kKBmNGI9mYRdPvtPsp6aAF9BJr7FlCCT4x3OHcXe3wXVswpWTvGKQ6qM6M9I\ncfRC/RvaUbZ23SwQ7B3Rse9GTHsT7yuniF01/G+kzZdwc/vNidlKCUA9wB8JSY84\nE/g2hHDsONLtOgcQC9XL1ako\n-----END PRIVATE KEY-----\n",
  "client_email": "datahub@aptee-353914.iam.gserviceaccount.com",
  "client_id": "118436377233006939242",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/datahub%40aptee-353914.iam.gserviceaccount.com"
}

gc = gspread.service_account_from_dict(auth)
@app.route('/', methods =['POST', 'GET'])
def home():
        sh = gc.open_by_url('https://docs.google.com/spreadsheets/d/1CyWjl6Y5Gi_e3z7A8wtw-qOaBe3GvCD4sqWWvaMubXY/edit?usp=sharing')
        wks=sh.worksheet("Client_Details")
        form = SignupForm(flask.request.form)
        if form.email_id.data:
                if form.email_id.data in wks.col_values(2):
                        pos =wks.find(form.email_id.data.lower())
                        if form.password.data!=wks.cell(pos.row,4).value:
                                return flask.render_template('index.html',form=form,message="Password incorrect")
                        else:
                                return flask.render_template('index.html',form=form,message="Logged in Successfully",id=wks.cell(pos.row,1).value)
                else:
                        time.sleep(random.randint(1,3))
                        id="CL"+datetime.now().strftime("%d%m%Y%H%M%S")
                        wks.append_row([id,form.email_id.data,form.name.data,form.password.data])
                        return flask.render_template('index.html',form=form,message="registration Successful!",id=id)
        else:
                return flask.render_template('index.html',form=form)
@app.route('/account_creation/<id>',methods=['GET','POST'])
def account(id):
        sh = gc.open_by_url('https://docs.google.com/spreadsheets/d/1CyWjl6Y5Gi_e3z7A8wtw-qOaBe3GvCD4sqWWvaMubXY/edit?usp=sharing')
        wks=sh.worksheet("Client_Details")
        form = SignupForm(flask.request.form)
        print(id)
        if wks.find(id):
                pos=wks.find(id)
                wks.update_cell(pos.row, 5, str(form.DOB.data))
                wks.update_cell(pos.row, 6, form.target.data)
                wks.update_cell(pos.row, 7, form.gender.data)
                wks.update_cell(pos.row, 8, form.college.data)
                wks.update_cell(pos.row, 9, form.college_location.data)
                wks.update_cell(pos.row, 10, form.course.data)
                wks.update_cell(pos.row, 11, form.semester.data)   
                return flask.render_template('register.html',form=form,id=id)
        else:
                return flask.render_template('index.html',form=form,message="error")
if __name__ == '__main__':
    app.run(debug = True)