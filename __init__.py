# import os 

# from flask import Flask, render_template
# from . import db
# from . import pond

# def create_app(test_config=None):
#   app = Flask(__name__, instance_relative_config=True)
#   app.config.from_pyfile('settings.cfg', silent=True)

#   try:
#     os.makedirs(app.instance_path)
#   except OSError:
#     pass
  
#   db.init_app(app)
#   app.register_blueprint(pond.bp)

#   @app.route('/index')
#   @app.route('/')
#   def index():
#     return "Tes"

#   @app.errorhandler(404)
#   def page_not_found(e):
#     # note that we set the 404 status explicitly
#     return "404"

#   return app