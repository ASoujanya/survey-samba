from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_migrate import Migrate

app = Flask(__name__)
db = SQLAlchemy()

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://survey_samba:survey_samba@localhost:5432/survey_samba"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
migrate = Migrate(app, db)

 
class client(db.Model):
    __tablename__ = 'client'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())

 