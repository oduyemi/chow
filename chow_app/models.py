from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from chow_app import db


class Menu_cat(db.Model):
    menu_cat_id = db.Column(db.Integer, autoincrement=True,primary_key=True)
    menu_cat = db.Column(db.String(200),nullable=False)
class Menu(db.Model):
    menu_id = db.Column(db.Integer, autoincrement=True,primary_key=True)
    menu_item = db.Column(db.String(200),nullable=False)
    menu_code = db.Column(db.String(200),nullable=False)
    menu_desc = db.Column(db.Text(),nullable=False)
    menu_cat = db.Column(db.Integer, db.ForeignKey('menu_cat.menu_cat_id'))
    menu_price = db.Column(db.Float(),nullable=False)
    menu_img = db.Column(db.String(200), nullable=False)
    menu_details = db.Column(db.Integer, db.ForeignKey('details.details_id'))



# class Cart(db.Model):
#     cart_id = db.Column(db.Integer, autoincrement=True,primary_key=True)
#     cart_menu = db.Column(db.Integer, db.ForeignKey('menu.menu_id'))
#     cart_qty = db.Column(db.Integer(),nullable=True)
#     cart_delivery= db.Column(db.Integer(),nullable=True)
    
    #RELATIONSHIP
    # cartdeets = db.relationship("Menu", backref="menu_deets")

class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey('menu.menu_id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False, default=0)
    user_id = db.Column(db.Integer, nullable=False)

    #RELATIONSHIP
    item = db.relationship('Menu', backref='cart_items')

    def __repr__(self):
        return f'<Cart {self.quantity} {self.item.name}>'


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'),  nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    delivery_address = db.Column(db.String(100), nullable=True)

    def __repr__(self):
        return f'<Order {self.id}>'

class Order_detail(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
    item_id = db.Column(db.Integer, db.ForeignKey('menu.menu_id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)

    #RELATIONSHIP
    order = db.relationship('Order', backref='order_detail')
    item = db.relationship('Menu')

    def __repr__(self):
        return f'<OrderDetail {self.item.name} x {self.quantity}>'


# class Delivery_option(db.Model):
#     delivery_id = db.Column(db.Integer, autoincrement=True,primary_key=True)
#     delivery_option = db.Column(db.String(120),nullable=False)

# class Order_status(db.Model):
#     order_status_id = db.Column(db.Integer, autoincrement=True,primary_key=True)
#     order_status = db.Column(db.String(120),nullable=False)


class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    user_fullname=db.Column(db.String(100),nullable=True)
    user_email = db.Column(db.String(50), nullable=False, unique=True)
    user_phone=db.Column(db.String(100),nullable=True)
    password_hash = db.Column(db.String(128), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    user_regdate = db.Column(db.DateTime(), default=datetime.utcnow)
    
    #RELATIONSHIP
    order = db.relationship('Order', backref='user', lazy=True)

    def __repr__(self):
        return f'<User {self.username}>'

class Admin(db.Model):
    admin_id = db.Column(db.Integer, primary_key=True)
    admin_fname=db.Column(db.String(100),nullable=True)
    admin_lname=db.Column(db.String(100),nullable=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password_hash = db.Column(db.String(128), nullable=False)
    admin_regdate = db.Column(db.DateTime(), default=datetime.utcnow)

    def __repr__(self):
        return f'<Admin {self.username}>'

class Payment(db.Model):
    payment_id = db.Column(db.Integer, primary_key=True)
    payment_order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
    date_paid = db.Column(db.DateTime, default=datetime.utcnow)
    amount = db.Column(db.Float, nullable=False)

    #RELATIONSHIP
    order = db.relationship('Order', backref='payment')

    def __repr__(self):
        return f'<Payment {self.amount}>'






# class Payment(db.Model):
#     payment_id = db.Column(db.Integer, autoincrement=True,primary_key=True)
#     payment_userfname = db.Column(db.String(200),nullable=True)   
#     payment_user = db.Column(db.Integer, db.ForeignKey('user.user_id'))
#     payment_amount = db.Column(db.Float(),nullable=True)
#     payment_menu = db.Column(db.Integer, db.ForeignKey('menu.menu_id'))
#     payment_date = db.Column(db.DateTime(), default=datetime.utcnow)
#     payment_status = db.Column(db.Integer, db.ForeignKey('p_status.p_status_id')) 

#     #Relationship
#     paydeets = db.relationship("P_status", backref="pdeets")


# class P_status(db.Model):
#     p_status_id = db.Column(db.Integer, autoincrement=True,primary_key=True)
#     p_status = db.Column(db.String(120),nullable=False)
  
class Contact(db.Model):
    contact_id=db.Column(db.Integer, autoincrement=True,primary_key=True) 
    contact_fullname=db.Column(db.String(150),nullable=False)   
    contact_phone=db.Column(db.String(40),nullable=False)
    contact_email=db.Column(db.String(100),nullable=False)
    contact_message=db.Column(db.Text(),nullable=False)
    contact_date = db.Column(db.DateTime(), default=datetime.utcnow)
    contact_admin=db.Column(db.Integer, db.ForeignKey('admin.admin_id'), nullable=False)

    #RELATIONSHIP
    # contactdeets = db.relationship("Contact", backref="admindeets")









