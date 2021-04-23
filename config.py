import os

class Config:

  '''
  General configurations parent class
  '''

  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://burens:Hawaii@localhost/pitch'
  SECRET_KEY = os.environ.get('SECRET_KEY')
  
  SQLALCHEMY_TRACK_MODIFICATIONS = False

  @staticmethod
  def init_app(app):
      pass

class ProdConfig(Config):
  '''
  Production  configuration child class

  Args:
      Config: The parent configuration class with General configuration settings
  '''
  pass

class DevConfig(Config):
  '''
  Development configuration child class
  
  Args:
      Config:The parent configuration class with General configuration settings
  '''

  DEBUG = True

config_options = {
    'development': DevConfig,
    'production': ProdConfig
}
