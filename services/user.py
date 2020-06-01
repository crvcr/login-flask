from flask_bcrypt import Bcrypt
bcrypt = Bcrypt()

from models import db, User

def getByUsername(username):
  user = User.query.filter_by(username=username).first()
  return user

def insert(username, password):
  admin_user = User(username=username, password=bcrypt.generate_password_hash(password))
  db.session.add(admin_user)
  db.session.commit()