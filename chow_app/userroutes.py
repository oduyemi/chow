import os, random, string
from flask import render_template, request, redirect, url_for, session, flash
from sqlalchemy.sql import text
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.exceptions import HTTPException
from chow_app import app, db
from chow_app.models import User, Contact, Order
from forms import ContactForm, LoginForm, SignUpForm


# def generate_name():
#     global filename
#     filename = random.sample(string.ascii_lowercase,10)
#     return ''.join(filename) 

#       --  ROUTES  --
@app.route('/', methods = ["POST", "GET"], strict_slashes = False)
def home():
    id =session.get("user")        
    if request.method == "POST":
        if session.get("user") != None:
            location = request.form.get("location")
            preference = request.form.get("preference")
            
            if location != "" and preference != "":
                new_order = Order(order_location=location, order_preference=preference, order_user=id)
                db.session.add(new_order)
                db.session.commit()
                return redirect(url_for("shop"))
            else:
                flash("Please select your location")
                return redirect("/")
        else:
            return redirect(url_for("login"))
    else:
        return render_template('user/index.html')
   

@app.route('/contact', methods = ["POST", "GET"], strict_slashes = False)
def contact():
    form = ContactForm()
    fullname = request.form.get("fullname")
    phone = request.form.get("phone")
    mail = request.form.get("mail")
    message=request.form.get("message")
    error = None
    if request.method == "GET":
        return render_template('user/contact.html', form=form, error=error, fname=fullname, phone=phone, mail=mail, message=message)
    else:
        try:
            if fullname !='' and phone != "" and mail !='' and message != "":
                new_contact=Contact(contact_name = fullname, contact_phone = phone, contact_email = mail, contact_content = message, contact_status_id=1)
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
def signup():
    form= SignUpForm()
    if request.method=="POST":
        fullname = request.form.get("fullname")
        phone = request.form.get("phone")
        email = request.form.get("email")
        password=request.form.get("password")
        hashedpwd = generate_password_hash(password)
        if fullname !='' and phone != "" and email != "" and password !='':
            new_user=User(user_fullname = fullname, user_phone = phone, user_email = email, user_password = hashedpwd)
            db.session.add(new_user)
            db.session.commit()
            userid=new_user.user_id
            session['user']=userid
            flash(f"Account created for you, '{fullname}'! Please proceed to LOGIN ", "success")
            return redirect(url_for('login'))
        else:
            flash('You must fill the form correctly to signup', "danger")
    else:
        return render_template('user/signup.html', form = form, title="Sign Up")

@app.route('/login', methods = ['POST', 'GET'], strict_slashes = False)
def login():
    form=LoginForm()
    if request.method=='GET':
        return render_template('user/login.html', form=form)
    else:
        mail=request.form.get('email')
        pwd=request.form.get('password')
        deets = db.session.query(User).filter(User.user_email==mail).first() 
        if deets !=None:
            pwd_indb = deets.user_password
            chk = check_password_hash(pwd_indb, pwd)
            if chk:
                id = deets.user_id
                session['user'] = id
                return redirect("shop")
            else:
                flash('Invalid password')
        return redirect(url_for('login'))


@app.route("/logout", strict_slashes = False)
def logout():
    if session.get("user") != None:
        session.pop("user",None)
    return redirect('/')



@app.route('/dashboard', methods = ['POST', 'GET'], strict_slashes = False)
def dashboard():
    id = session.get("user")
    if id != None:
        return render_template("user/dashboard.html")
    else:
        return redirect(url_for("login"))


@app.route("/shop", strict_slashes = False)
def shop():
    id = session.get("user")
    if request.method == "GET":
        return render_template('user/shop.html', title="Shop Now")