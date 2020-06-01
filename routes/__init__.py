from .main import main_bp
from .api import api_bp
from .auth import auth_bp

from flask import redirect

def init_app(app):
  @app.errorhandler(404)
  def not_found(error):
    """Page not found."""
    return redirect('/')

  app.register_blueprint(main_bp)
  app.register_blueprint(auth_bp)
  app.register_blueprint(api_bp, url_prefix='/api')