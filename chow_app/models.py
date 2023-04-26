from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from chow_app import db



class Menu(db.Model):
    menu_id = db.Column(db.Integer, autoincrement=True,primary_key=True)
    menu_item = db.Column(db.String(200),nullable=False)
    menu_code = db.Column(db.String(200),nullable=False)
    menu_desc = db.Column(db.Text(),nullable=False)
    menu_cat_id = db.Column(db.Integer, db.ForeignKey('menu_cat.menu_cat_id'))
    menu_price = db.Column(db.Float(),nullable=False)
    menu_img = db.Column(db.String(200), nullable=False)
    menu_details = db.Column(db.Integer, db.ForeignKey('details.details_id'))

class Menu_cat(db.Model):
    menu_cat_id = db.Column(db.Integer, autoincrement=True,primary_key=True)
    menu_cat = db.Column(db.String(200),nullable=False)

class Cart(db.Model):
    cart_id = db.Column(db.Integer, autoincrement=True,primary_key=True)
    cart_menu = db.Column(db.Integer, db.ForeignKey('menu.menu_id'))
    cart_qty = db.Column(db.Integer(),nullable=True)
    cart_delivery= db.Column(db.Integer(),nullable=True)
    
    #RELATIONSHIP
    cartdeets = db.relationship("Menu", backref="menu_deets")

class Order(db.Model):
    order_id = db.Column(db.Integer, autoincrement=True,primary_key=True)
    order_amt = db.Column(db.Float(),nullable=True)
    order_user = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    order_ref = db.Column(db.String(200),nullable=True)
    order_date = db.Column(db.DateTime(), default=datetime.utcnow)
    order_status = db.Column(db.Integer, db.ForeignKey('order_status.order_status_id'))

class Order_details(db.Model):
    __tablename__="details"
    details_id = db.Column(db.Integer, autoincrement=True,primary_key=True)
    details_location = db.Column(db.String(200),nullable=True)
    details_preference = db.Column(db.Integer, db.ForeignKey('delivery_option.delivery_id')) 
    details_item1 = db.Column(db.String(200),nullable=False)
    details_qty1 = db.Column(db.Integer(),nullable=False) 
    details_item2 = db.Column(db.String(200),nullable=True)
    details_qty2 = db.Column(db.Integer(),nullable=True) 
    details_item3 = db.Column(db.String(200),nullable=True)
    details_qty3 = db.Column(db.Integer(),nullable=True) 
    details_item4 = db.Column(db.String(200),nullable=True)
    details_qty4 = db.Column(db.Integer(),nullable=True) 
    details_item5 = db.Column(db.String(200),nullable=True)
    details_qty5 = db.Column(db.Integer(),nullable=True) 
    details_item6 = db.Column(db.String(200),nullable=True)
    details_qty6 = db.Column(db.Integer(),nullable=True) 
    details_item7 = db.Column(db.String(200),nullable=True)
    details_qty7 = db.Column(db.Integer(),nullable=True) 
    details_item8 = db.Column(db.String(200),nullable=True)
    details_qty8 = db.Column(db.Integer(),nullable=True) 
    details_item9 = db.Column(db.String(200),nullable=True)
    details_qty9 = db.Column(db.Integer(),nullable=True) 
    details_item10 = db.Column(db.String(200),nullable=True)
    details_qty10 = db.Column(db.String(200),nullable=True)
    details_qty10 = db.Column(db.Integer(),nullable=True) 
    details_amt = db.Column(db.Float(),nullable=False)
    details_user = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    details_qty1 = db.Column(db.Integer(),nullable=True) 
    details_amt = db.Column(db.Float(),nullable=True)


    #Relationship
    detailsdeets = db.relationship("Menu", backref="menudeets")


class Delivery_option(db.Model):
    delivery_id = db.Column(db.Integer, autoincrement=True,primary_key=True)
    delivery_option = db.Column(db.String(120),nullable=False)

class Order_status(db.Model):
    order_status_id = db.Column(db.Integer, autoincrement=True,primary_key=True)
    order_status = db.Column(db.String(120),nullable=False)


class User(db.Model):
    user_id=db.Column(db.Integer, autoincrement=True,primary_key=True)
    user_fullname=db.Column(db.String(100),nullable=True)
    user_phone=db.Column(db.String(100),nullable=True)
    user_email=db.Column(db.String(100),nullable=True, unique=True)
    user_password=db.Column(db.String(200),nullable=True)
    user_location=db.Column(db.String(200),nullable=True)
    user_regdate = db.Column(db.DateTime(), default=datetime.utcnow)

    #Relationship
    userdeets = db.relationship("Order_details", backref="details_deets")


class Payment(db.Model):
    payment_id = db.Column(db.Integer, autoincrement=True,primary_key=True)
    payment_userfname = db.Column(db.String(200),nullable=True)   
    payment_user = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    payment_amount = db.Column(db.Float(),nullable=True)
    payment_menu = db.Column(db.Integer, db.ForeignKey('menu.menu_id'))
    payment_date = db.Column(db.DateTime(), default=datetime.utcnow)
    payment_status = db.Column(db.Integer, db.ForeignKey('p_status.p_status_id')) 

    #Relationship
    paydeets = db.relationship("P_status", backref="pdeets")


class P_status(db.Model):
    p_status_id = db.Column(db.Integer, autoincrement=True,primary_key=True)
    p_status = db.Column(db.String(120),nullable=False)
  

class Admin(db.Model):
    admin_id=db.Column(db.Integer, autoincrement=True,primary_key=True)
    admin_fname=db.Column(db.String(100),nullable=True)
    admin_lname=db.Column(db.String(100),nullable=True)
    admin_username=db.Column(db.String(100),nullable=True, unique=True)
    admin_password=db.Column(db.String(200),nullable=True)
    admin_regdate = db.Column(db.DateTime(), default=datetime.utcnow)

class Contact(db.Model):
    contact_id=db.Column(db.Integer, autoincrement=True,primary_key=True) 
    contact_fullname=db.Column(db.String(150),nullable=False)   
    contact_phone=db.Column(db.String(40),nullable=False)
    contact_email=db.Column(db.String(100),nullable=False)
    contact_message=db.Column(db.Text(),nullable=False)
    contact_date = db.Column(db.DateTime(), default=datetime.utcnow)
    contact_admin_id=db.Column(db.Text(),nullable=True)

    # #RELATIONSHIP
    # contactdeets = db.relationship("Contact", backref="admindeets")









