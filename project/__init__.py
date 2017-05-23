from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_modus import Modus
import os

app = Flask(__name__)
modus = Modus(app)

if os.environ.get('ENV') == 'production':
    debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
else:
    debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost/owners_mvc'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
db = SQLAlchemy(app)

from project.owners.views import owners_blueprint
from project.pets.views import pets_blueprint

app.register_blueprint(owners_blueprint, url_prefix='/owners')
app.register_blueprint(pets_blueprint, url_prefix='/owners/<int:owner_id>/pets')

@app.route('/')
def root():
	return 'Hello Blueprints!'

