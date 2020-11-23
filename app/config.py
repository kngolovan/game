"""Configuration for the application."""
import os


SQLALCHEMY_DATABASE_URI = os.environ["SQLALCHEMY_DATABASE_URI"]
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = os.environ["SECRET_KEY"]
