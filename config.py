class DevelopmentConfig():
    HOST = '0.0.0.0'
    PORT = 5000
    DEBUG = True
    CELERY_BROKER_URL = 'redis://localhost:6379/0'
    CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'

    @staticmethod
    def init_app(app):
        pass

config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}
