# import os
# from flask import Flask

# # Initialize the app
# app = Flask(__name__, instance_relative_config=True)

# # Load the views
# from app import views

# # Load the config file
# app.config.from_object('config')

# app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# local imports
from config import app_config

# db variable initialization
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    db.init_app(app)
    # temporary route
    @app.route('/')
    def hello_world():
        return 'Hello, World!'
    app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))
    return app

    
