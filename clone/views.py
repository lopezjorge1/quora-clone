from flask import Flask,redirect,request,render_template,url_for
from flask_sqlalchemy import SQLAlchemy
from clone import app,db
import os

'''
@app.route('/')
def index():
    return 'Hello World!'
'''

@app.route('/',methods=['GET','POST'])
def home():
    return render_template('base.html')

#answer page
#login page - will require oauth/auth

#in the homepage there are two buttons and a search bar
#the two buttons: notifications and add question
#add question button will popup with a form
#notifications button will popup with previous notifications and lead to older
#search bar will search for content (no need to redirect because I won't have all of the content)
