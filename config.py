import os
 
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://lilian:12345@localhost/pitch'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    UPLOADED_PHOTOS_DEST ='app/static/photos'

    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

class ProdConfig(Config):
    pass

# class DevConfig(Config):
    
#     DEBUG = True
   
class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://lilian:12345@localhost/pitch'
class DevConfig(Config):
   SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://lilian:12345@localhost/pitch'
   DEBUG = True



config_option = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}   