from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('config.py', silent = False)
db = SQLAlchemy(app)

from chow_app import adminroutes, userroutes


import os, random, string
from flask import render_template, request, redirect, url_for, session, flash
from sqlalchemy.sql import text
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.exceptions import HTTPException
from chow_app import app, db
from chow_app.models import User, Contact, Payment, Tour, Trip, Question


def generate_name():
    global filename
    filename = random.sample(string.ascii_lowercase,10)
    return ''.join(filename) 

#       --  ROUTES  --

@app.route('/', strict_slashes = False)
def home():
    return render_template('user/index.html')


@app.route('/contact', methods = ["POST", "GET"], strict_slashes = False)
def contact():
    name = request.form.get("c_name")
    phone = request.form.get("phone")
    email = request.form.get("email")
    gender=request.form.get("gender")
    method=request.form.get("method")
    message=request.form.get("message")
    error = None
    try:
        if not name or not name.strip():
            error = "Fields cannot be blank. Please provide a valid name"
        if not email or not email.strip():
            error = "fields cannot be blank. Please provide a valid email address"
        if not phone or not phone.strip():
            error = "Fields cannot be blank. Please provide a valid phone number"
        if not gender or not gender.strip():
            error = "Fields cannot be blank. Please choose your gender"
        if not method or not method.strip():
            error = "Fields cannot be blank. Please tell us how you would like to be contacted"
        if not message or not message.strip():
            error = "Fields cannot be blank. Please drop a message"

        if request.method == "GET":
            return render_template('user/contact.html', error=error, name=name, phone=phone, email=email, gender=gender, method=method, message=message)
        else:
            
            if name !='' and phone != "" and email !='' and gender !='' and method != "" and message != "":
                new_contact=Contact(contact_name = name, contact_phone = phone, contact_email = email, contact_gender = gender, contact_method = method, contact_content = message, contact_status_id=1)
                db.session.add(new_contact)
                db.session.commit()
                flash(f"Thank you for reaching out to us, We will get in touch with you shortly. ", "success")
                return redirect(url_for("contact"))
    except:
        ""

@app.route('/about', strict_slashes = False)
def about():
    return render_template('user/about.html')

@app.route('/signup', methods = ["POST", "GET"], strict_slashes = False)
def usersignup():
    if request.method == "GET":
        return render_template('user/signup.html', title="Sign Up")
    else:
        fullname = request.form.get("fullname")
        phone = request.form.get("phone")
        username = request.form.get("username")
        password=request.form.get("password")
        hashedpwd = generate_password_hash(password)
        if fullname !='' and phone != "" and username !='' and password !='':
            new_user=User(user_fullname = fullname, user_phone = phone, user_username = username,
            user_password = hashedpwd)
            db.session.add(new_user)
            db.session.commit()
            userid=new_user.user_id
            session['user']=userid
            flash(f"Account created for '{fullname}'! Please proceed to LOGIN ", "success")
            return redirect(url_for('userlogin'))
        else:
            flash('You must fill the form correctly to signup', "danger")
    # return render_template('user/signup.html')


@app.route('/login', methods = ['POST', 'GET'], strict_slashes = False)
def userlogin():
    if request.method=='GET':
        return render_template('user/login.html')
    else:
        username=request.form.get('username')
        pwd=request.form.get('password')
        deets = db.session.query(User).filter(User.user_username==username).first() 
        if deets !=None:
            pwd_indb = deets.user_password
            chk = check_password_hash(pwd_indb, pwd)
            if chk:
                id = deets.user_id
                session['user'] = id
                return redirect(url_for('account'))
            else:
                flash('Invalid password')
        return redirect(url_for('userlogin'))


@app.route('/login', methods = ['POST', 'GET'], strict_slashes = False)
def passwordreset():
    if request.method=='GET':
        return render_template('user/login.html')
    else:
        username=request.form.get('username')


@app.route("/logout", strict_slashes = False)
def userlogout():
    if session.get("user") != None:
        session.pop("user",None)
    return redirect('/login')