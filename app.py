#importing required packages
import pygsheets
import json
from flask import Flask, render_template
from flask_login import UserMixin
from flask_wtf import wtforms
from wtforms import StringField,PasswordField,SubmitField

gc = pygsheets.authorize(service_file = 'Auth.json')
sh = gc.open_by_url('https://docs.google.com/spreadsheets/d/1CyWjl6Y5Gi_e3z7A8wtw-qOaBe3GvCD4sqWWvaMubXY/edit?usp=sharing')
wks = sh.worksheet_by_title('Sheet1')
#for row in wks:
 #       print(row)
app = Flask(__name__, template_folder="Templates")
app.config['SECRET_KEY']='abcdefghijkhlmnop'
@app.route('/', methods =['POST', 'GET'])
def home():
        return render_template('index.html')

@app.route('/login',methods=['POST','GET'])
def login():
        return render_template('login.html')
if __name__ == '__main__':
    app.run(debug = True)