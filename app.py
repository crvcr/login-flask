from flask import Flask

import config
import models
import routes
import services

def init_app(app):
  with app.app_context():
    config.init_app(app)
    models.init_app(app)
    routes.init_app(app)
    services.init_app(app)

    # -- <testing user> -----------------------------------------------
    admin_user = services.user_service.getByUsername('admin')
    if admin_user is None:
      services.user_service.insert('admin','admin')
    # -- </testing user> ----------------------------------------------

  app.run(debug=True, port=3000)
  
# -- __main__ ------------------------------------------------------
if (__name__ == '__main__'):
  app = Flask(__name__)
  init_app(app)