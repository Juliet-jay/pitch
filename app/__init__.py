from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options


# initializing application
app = Flask (__name__)

#Creating the app configurations
app.config.from_object(config_options[config_name])