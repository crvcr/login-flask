from flask import Blueprint, jsonify, request
from flask_bcrypt import Bcrypt

import models

auth_bp = Blueprint('auth_bp', __name__)
bcrypt = Bcrypt()

def validate_password(hashedPassword, password):
  return bcrypt.check_password_hash(hashedPassword, password)

def validate_user(username='', password=''):
  user = models.User.query.filter_by(username=username).first()
  if user is None:
    return False
  else:
    return validate_password(user.password, password)