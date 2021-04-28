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
  SQLALCHEMY_DATABASE_URI = "postgresql://fjikbwgaapaotj:cfc044c1cc142579b10b31a9d3eb47afea5cb70e9cd55d85280f85e07b0c6795@ec2-3-217-219-146.compute-1.amazonaws.com:5432/d8eq4dch6e21bh?sslmode=require"

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