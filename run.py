#!/home/md-ibrahim/anaconda3/envs/pintarmind_env/bin/python

from sys import exit
from decouple import config

from apps.config import config_dict
from apps import create_app, db

from gevent.pywsgi import WSGIServer


get_config_mode = config('RELEASE_TYPE', default='Debug')

try:
    # Load the configuration using the default values
    app_config = config_dict[get_config_mode.capitalize()]
    print(app_config)

except KeyError:
    exit('Error: Invalid <config_mode>. Expected values [Debug, Production] ')

app = create_app(app_config)

def kill_server():
        print('You pressed Ctrl+C!')
        http_server.stop()
        exit(0)

if get_config_mode == "Debug" :
    app.logger.info('DEBUG       = ' + 'True')
    app.logger.info('Environment = ' + get_config_mode)
    app.logger.info('DBMS        = ' + app_config.MONGODB_SETTINGS["host"])

    if __name__ == "__main__":
        http_server = app.run(host=app_config.IPADDRESS, port=int(app_config.PORT), threaded=True, debug=True)

else:
    if __name__ == "__main__":
        http_server = WSGIServer((app_config.IPADDRESS, int(app_config.PORT)), app)
        print("\nRunning on {}:{}...\n".format(app_config.IPADDRESS, app_config.PORT))

        try:
            http_server.serve_forever()
        except KeyboardInterrupt:
            kill_server()