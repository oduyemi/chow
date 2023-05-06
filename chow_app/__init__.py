from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('config.py', silent = False)
db = SQLAlchemy(app)

app.cart = {}

from chow_app import adminroutes, userroutes, paystack

