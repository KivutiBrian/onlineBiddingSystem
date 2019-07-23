class Config(object):
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:password@127.0.0.1:5432/onlineBiddingSystem'
    SECRET_KEY = 'some=secret-key'

class ProductionConfig(Config):
    DEBUG = False
