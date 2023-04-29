import os, random, string, json
from flask import render_template, request, redirect, url_for, session, flash, jsonify
from sqlalchemy.sql import text
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.exceptions import HTTPException
from chow_app import app, db
from chow_app.models import User, Contact, Order, Menu
from forms import ContactForm, LoginForm, SignUpForm


mysql = MySQL(app)
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "chowdb"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"



@app.route("/livesearch", methods = ["POST", "GET"])
def livesearch():
    searchbox = request.form.get("text")
    cursor = mysql.connection.cursor()
    #items = Menu.query.filter(Menu.menu_item.like("{}%")).order_by(Menu.menu_item).all()
    query = "SELECT menu_item FROM menu WHERE menu_item LIKE '{}%' ORDER BY menu_item".format(searchbox)
    cursor.execute(query)
    result = cursor.fetchall()
    return jsonify(result)


# def generate_name():
#     global filename
#     filename = random.sample(string.ascii_lowercase,10)
#     return ''.join(filename)
# 
# def array_merge( first_array , second_array ):
#     if isinstance( first_array , list ) and isinstance( second_array , list ):
#         return first_array + second_array

#     elif isinstance( first_array , dict ) and isinstance( second_array , dict ):
# 	    return dict( list( first_array.items() ) + list( second_array.items() ) )
    
#     elif isinstance( first_array , set ) and isinstance( second_array , set ):
#         return first_array.union( second_array )
	
#     else:
#         return False	 

#       --  ROUTES  --
@app.route('/', methods = ["POST", "GET"], strict_slashes = False)
def home():
    id =session.get("user")
    main_ = db.session.query(Menu).filter(Menu.menu_cat_id==1).all()
    protein_ = db.session.query(Menu).filter(Menu.menu_cat_id==2).all()
    swallow_ = db.session.query(Menu).filter(Menu.menu_cat_id==3).all()
    soup_ = db.session.query(Menu).filter(Menu.menu_cat_id==4).all()         
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
        return render_template('user/index.html', main_=main_, swallow_=swallow_, protein_=protein_, soup_=soup_)



   

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


@app.route("/buffet", strict_slashes = False)
def buffet():
    return render_template("user/buffet.html")


@app.route("/outdoor", strict_slashes = False)
def outdoor():
    return render_template("user/outdoor.html")


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


@app.route("/search/<item>", strict_slashes = False)
def search(item):
    item = request.form.get("")
    if item:
    id = db.session.query(Menu.menu_id).get()
    content = Menu.query.filter(Menu.menu_item==item)
    return redirect("/add/id")



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
    main_ = db.session.query(Menu).filter(Menu.menu_cat_id==1).all()
    protein_ = db.session.query(Menu).filter(Menu.menu_cat_id==2).all()
    swallow_ = db.session.query(Menu).filter(Menu.menu_cat_id==3).all()
    soup_ = db.session.query(Menu).filter(Menu.menu_cat_id==4).all() 
    if request.method == "GET":
        return render_template('user/shop.html', title="Shop Now", main_=main_, protein_=protein_, swallow_=swallow_, soup_=soup_)


@app.route('/add/<bid>', methods=['GET', 'POST'], strict_slashes = False)
def add_to_cart(bid):
    id = session.get("user")
    mdeets = db.session.query(Menu).filter(Menu.menu_id==bid).one()
    price = float(mdeets.menu_price) + 200.00
    extra = db.session.query(Menu).filter(Menu.menu_cat_id==5).all()
    protein_ = db.session.query(Menu).filter(Menu.menu_cat_id==2).all()

    if id != None:
        if request.method == "GET":
            return render_template('user/add.html', title="Add to Cart", mdeets=mdeets, price=price, extra=extra, protein_=protein_)
        else:
            return render_template('user/add.html', title="Add to Cart", mdeets=mdeets, price=price, extra=extra, protein_=protein_)

    else:
        return redirect(url_for("login"))


@app.route("/checkout", strict_slashes = False)
def checkout():
    return render_template("user/checkout.html")
# 	try:
# 		qty = int(request.form['quantity'])
# 		_code = request.form['code']
# 		# validate the received values
# 		if qty and _code and request.method == 'POST':
# 			query = ("SELECT * FROM menu WHERE code=%s", _code)
# 			row = db.session.execute.fetchone(query)
			
# 			itemArray = { row['code'] : {'name' : row['name'], 'code' : row['code'], 'quantity' : qty, 'price' : row['price'], 'image' : row['image'], 'total_price': qty * row['price']}}
			
# 			all_total_price = 0
# 			all_total_qty = 0
			
# 			session.modified = True
# 			if 'cart_item' in session:
# 				if row['code'] in session['cart_item']:
# 					for key, value in session['cart_item'].items():
# 						if row['code'] == key:
# 							#session.modified = True
# 							#if session['cart_item'][key]['quantity'] is not None:
# 							#	session['cart_item'][key]['quantity'] = 0
# 							old_qty = session['cart_item'][key]['quantity']
# 							total_qty = old_qty + qty
# 							session['cart_item'][key]['quantity'] = total_qty
# 							session['cart_item'][key]['total_price'] = total_qty * row['price']
# 				else:
# 					session['cart_item'] = array_merge(session['cart_item'], itemArray)

# 				for key, value in session['cart_item'].items():
# 					individual_qty = int(session['cart_item'][key]['quantity'])
# 					individual_price = float(session['cart_item'][key]['total_price'])
# 					all_total_qty = all_total_qty + individual_qty
# 					all_total_price = all_total_price + individual_price
# 			else:
# 				session['cart_item'] = itemArray
# 				all_total_qty = all_total_qty + qty
# 				all_total_price = all_total_price + qty * row['price']
			
# 			session['all_total_qty'] = all_total_qty
# 			session['all_total_price'] = all_total_price
			
# 			return redirect(url_for('.products'))
# 		else:			
# 			return 'Error while adding item to cart'
# 	except Exception as e:
# 		print(e)
# 	finally:
# 		cursor.close() 
# 		conn.close()


@app.route("/cart", methods = (["POST", "GET"]), strict_slashes = False)
def cart():
    id = session.get("user")
    if id != None:
        if request.method == "GET":
            return render_template('user/goto_cart.html', title="Cart") 


@app.route("/past_orders", methods =(["POST", "GET"]), strict_slashes = False)
def past():
    id = session.get("user")
    if id != None:
        return render_template("user/past_orders.html")