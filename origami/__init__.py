from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = 'eebb2c58cc974ff7833f182cc71dfd9e'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.debug = False
app.config['SQLALCHEMY_DATABASE_URI'] = ' postgres://myhltsfhuflsop:5529ecc6b7ce36c71a3b2a4a23668d022c788a2f5c4679b7e2a1b45e476ecc40@ec2-54-147-36-107.compute-1.amazonaws.com:5432/d1jt0bcpn86610'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'jeffery1996.jbw@gmail.com'
app.config['MAIL_PASSWORD'] = 'gislqtjykjisgusv'
mail = Mail(app)

from origami import routes