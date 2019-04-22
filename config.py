import os
 
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://lilian:12345@localhost/watchlist'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True
   

config_option = {
'development':DevConfig,
'production':ProdConfig
}   