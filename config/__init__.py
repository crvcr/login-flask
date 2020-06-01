from flask_bcrypt import Bcrypt

def init_app(app):
  app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/database.db'
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
  app.config['BCRIPT_LOG_ROUNDS'] = 15
  bcrypt = Bcrypt(app)