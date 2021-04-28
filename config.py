import os

class Config:

  '''
  General configurations parent class
  '''

  
  SECRET_KEY = os.environ.get('SECRET_KEY')
  UPLOADED_PHOTOS_DEST = 'app/static/photos'

  SQLALCHEMY_TRACK_MODIFICATIONS = False

  #  email configurations
  MAIL_SERVER = 'smtp.googlemail.com'
  MAIL_PORT = 587
  MAIL_USE_TLS = True
  MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
  MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

  @staticmethod
  def init_app(app):
      pass

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://burens:Hawaii@localhost/pitch_test'

class ProdConfig(Config):
  '''
  Production  configuration child class

  Args:
      Config: The parent configuration class with General configuration settings
  '''
  SQLALCHEMY_DATABASE_URI = "postgresql://ncydlznvquwihs:fb7d47b52a8b9f8f73f70c56e1759df967fa83895a0e6fd0d20ddef74b0bc482@ec2-54-166-167-192.compute-1.amazonaws.com:5432/d27ag75eq27pg?sslmode=require"

class DevConfig(Config):
  '''
  Development configuration child class
  
  Args:
      Config:The parent configuration class with General configuration settings
  '''

  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://burens:Hawaii@localhost/pitch'

  DEBUG = True

config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'test':TestConfig
}
