from flask import Blueprint, jsonify, request
import services

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/authenticate', methods = ['POST'])
def authenticate():
  user = request.json
  response = {'ok': False, 'error': 'Username o password incorrectos'}

  is_valid_user = services.auth_service.validate_user(user['username'], user['password'])

  if(is_valid_user):
    response = {
      'ok': True, 
      'data': {
        'message': 'Autenticado correctamente'
      }
    }

  return jsonify(response)