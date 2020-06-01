from flask import Blueprint, send_file, render_template

main_bp = Blueprint('main_bp', __name__)
  
@main_bp.route('/')
def index():
  return render_template('index.html')

@main_bp.route('/login')
def login():
  return send_file('templates/login.html')