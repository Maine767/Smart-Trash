from flask import Flask, request, render_template, json
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from threading import Timer
from sklearn.linear_model import LinearRegression
from PIL import Image, ImageDraw
from route import app_route
from ettities import _logger, Panel

app = Flask(__name__, template_folder='template', static_folder="static")

def log_fillment():
    _logger.insert_data(Panel.get_objects())

    Timer(30, log_fillment).start()

log_fillment()

app.register_blueprint(app_route)

@app.route('/connect')
def connect():

    cursor = _logger.read_data('fillment')
    time = []
    avg_fill = []

    counter = 0
    for item in cursor:
        time.append(item['timestamp'])
        counter = 0
        f = []
        for i in item:
            if counter >= 2:
                f.append(item[i]["fillment"])
            counter += 1

        avg_fill.append(np.average(f))

    x = np.arange(0, len(time)).reshape((-1, 1))
    y = np.array(avg_fill)

    plt.plot(x, y)
    plt.xticks(rotation=90)
    plt.ylim(0, 1)
    plt.savefig("source.png")

    model = LinearRegression().fit(x, y)
    x = np.arange(len(time), len(time) * 2).reshape((-1, 1))
    y_pred = model.predict(x)
    plt.plot(x, y_pred)
    plt.xticks(rotation=90)
    plt.savefig("predict.png")

    try:
        id = int(request.args.get('id', ''))
        amount = int(request.args.get("amount",""))
        Panel.set_trash(id, amount)
    except ValueError:
        print("Value/Values are incorrect")

    _logger.insert_data(Panel.get_objects())

    return json.dumps({'Проблема': request.args.get('id', ''), 'Координаты': request.args.get("coordinates", ''), 'Кол-во бутылок': request.args.get("amount", '')})


if __name__ == '__main__':
    app.run()
