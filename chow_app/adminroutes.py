import os, random, string
from flask import render_template, request, redirect, url_for, session, flash
from sqlalchemy.sql import text
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.exceptions import HTTPException
from chow_app import app, db
from chow_app.models import Admin, Contact, Order, Menu
from forms import LoginForm, AdminSignUpForm




@app.route('/admin/signup', methods = ["POST", "GET"], strict_slashes = False)
def adminsignup():
    form= AdminSignUpForm()
    if request.method=="POST":
        fname = request.form.get("fname")
        lname = request.form.get("lname")
        phone = request.form.get("phone")
        email = request.form.get("email")
        password=request.form.get("password")
        hashedpwd = generate_password_hash(password)
        if fname !='' and lname !="" and phone != "" and email != "" and password !='':
            new_admin=Admin(admin_fname = fname, admin_lname = lname, admin_phone = phone, admin_email = email, admin_password = hashedpwd)
            db.session.add(new_admin)
            db.session.commit()
            adminid=new_admin.admin_id
            session['admin']=adminid
            flash(f"Account created for you, '{fname}'! Please proceed to LOGIN ", "success")
            return redirect(url_for('adminlogin'))
        else:
            flash('You must fill the form correctly to signup', "danger")
    else:
        return render_template('admin/signup.html', form = form, title="Sign Up")

@app.route('/admin/login', methods = ['POST', 'GET'], strict_slashes = False)
def adminlogin():
    form=LoginForm()
    if request.method=='GET':
        return render_template('admin/login.html', form=form)
    else:
        mail=request.form.get('email')
        pwd=request.form.get('password')
        deets = db.session.query(Admin).filter(Admin.admin_email==mail).first() 
        if deets != None:
            pwd_indb = deets.admin_password
            chk = check_password_hash(pwd_indb, pwd)
            if chk:
                id = deets.admin_id
                session['admin'] = id
                return redirect("admindashboard")
            else:
                flash('Invalid password')
        return redirect(url_for('adminlogin'))


@app.route("/admin/logout", strict_slashes = False)
def adminlogout():
    if session.get("admin") != None:
        session.pop("admin",None)
    return redirect('/admin')



@app.route('/admin/dashboard', methods = ['POST', 'GET'], strict_slashes = False)
def admindashboard():
    id = session.get("admin")
    if id != None:
        return render_template("admin/dashboard.html")
    else:
        return redirect(url_for("adminlogin"))



@app.route('/admin', methods = ["POST", "GET"], strict_slashes = False)
def admin():
    id =session.get("admin")
    if id != None:
        return redirect(url_for("adminlogin"))
    else:
        return redirect(url_for("admindashboard"))