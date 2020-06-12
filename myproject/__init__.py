import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate



app = Flask(__name__)
app.config['SECRET_KEY'] = 'super_car_blondie'

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)


from myproject.posts.view import posts_blueprint
from myproject.contacts.view import contact_blueprint
from myproject.errors.handlers import error_blueprint


app.register_blueprint(posts_blueprint, url_prefix='/posts')
app.register_blueprint(contact_blueprint, url_prefix='/contacts')
app.register_blueprint(error_blueprint, url_prefix='/errors')