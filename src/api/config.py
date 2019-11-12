import os

class Config:
    GENERAL = {
        'host': os.environ['HOST'],
        'port': os.environ['PORT'],
        'threaded': 0,
        'username':os.environ['USERNAME'],
        'password':os.environ['PASSWORD']
    }

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

config = {
'development': DevelopmentConfig,
'production': ProductionConfig,
'default': DevelopmentConfig
}
