from flask import Flask, request, json
from threading import Timer
import sys
import os

sys.path.insert(1, os.path.join(sys.path[0], "../tests"))

from route import app_route
from tests import _logger, Panel

app = Flask(__name__, template_folder='template', static_folder="static")

def log_fillment():
    _logger.insert_data(Panel.get_objects())
    print(Panel.new_charts(_logger))
    Timer(30, log_fillment).start()

log_fillment()

app.register_blueprint(app_route)

if __name__ == '__main__':
    app.run()