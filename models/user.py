from models import db

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(200), unique=True)
  password = db.Column(db.String(200))