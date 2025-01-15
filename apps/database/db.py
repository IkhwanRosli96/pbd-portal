import mongoengine as db
from decouple import config
from apps.config import config_dict


get_config_mode = config('RELEASE_TYPE', default='Debug')

try:
    # Load the configuration using the default values
    app_config = config_dict[get_config_mode.capitalize()]
except KeyError:
    exit('Error: Invalid <config_mode>. Expected values [Debug, Production] ')

def initialize_db():
   db.connect('pbd_dev', host=app_config.MONGODB_SETTINGS["host"])
   return db