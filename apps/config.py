import os
from decouple import config

class Config(object):
    basedir = os.path.abspath(os.path.dirname(__file__))

    # Set up the App SECRET_KEY
    SECRET_KEY = config('SECRET_KEY', default='S#perS3crEt_007')
    SESSION_TYPE = 'filesystem'

    # MongoDB Connection
    MONGODB_SETTINGS = {'host': '{}://{}:{}@{}'.format(
        config('DB_ENGINE', default='mongodb+srv'),
        config('DB_USER', default='cairo'),
        config('DB_PASSWORD', default='iman2dina'),
        config('DB_HOST', default="cluster0.qc0smnu.mongodb.net")
        )
    }
    IPADDRESS = "0.0.0.0"
    PORT = "8080"


class ProductionConfig(Config):
    basedir = os.path.abspath(os.path.dirname(__file__))
    DEBUG = False

    # Set up the App SECRET_KEY
    SECRET_KEY = config('SECRET_KEY', default='S#perS3crEt_007')
    SESSION_TYPE = 'filesystem'

    # Security
    SESSION_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_DURATION = 3600

    # MongoDB Connection
    MONGODB_SETTINGS = {'host': '{}://{}:{}@{}'.format(
        config('DB_ENGINE', default='mongodb+srv'),
        config('DB_USER', default='cairo'),
        config('DB_PASSWORD', default='iman2dina'),
        config('DB_HOST', default="cluster0.qc0smnu.mongodb.net")
        )
    }

    IPADDRESS = "0.0.0.0"
    PORT = "9000"


class DebugConfig(Config):
    DEBUG = True

# Load all possible configurations
config_dict = {
    'Production': ProductionConfig,
    'Debug': DebugConfig
}
