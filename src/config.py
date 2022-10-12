from distutils.debug import DEBUG
from decouple import config


class Config:
    SECRET_KEY = config('ejfzekfj')


class DevelopmentConfig(Config):
    DEBUG = True


config = {
    'development': DevelopmentConfig
}
