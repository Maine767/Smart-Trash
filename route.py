from flask import render_template
import numpy as np
import logger
from sklearn.linear_model import LinearRegression
from PIL import Image, ImageDraw
from flask import Blueprint
from ettities import _logger, Panel

app_route = Blueprint('route', __name__)

@app_route.route('/choose')
def choose():
    ids = list()
    for i in range(len(Panel.get_objects())):
        ids.append(i+1)
    return render_template('choose.html', ids=ids)


@app_route.route('/create_new_sensor/settings')
def set_setting(id):
    pass


@app_route.route('/create_new_sensor')
def create_new_sensor():
    pass
    # return render_template('create.html')


@app_route.route('/check_statistic')
def statistic():
    cursor = _logger.read_data('fillment')
    print(cursor)
    time = []
    avg_fill = []
    last = cursor[len(cursor)][len(len(cursor))]
    print(last)

    avg_fill.append(np.average(last))
    return render_template('stats.html', image_path="", image_path_2="", AVG=avg_fill)


@app_route.route('/profile')
def profile():
    # sensors = pd.DataFrame(Panel.get_objects())
    return render_template('Profile.html', id_panel=Panel.get_unit_id(), sensors="In work", active_sensors="In work", mean_fill="In work")


@app_route.route('/<int:id>')
def interface(id):
    sensor = Panel.get_object(id)
    
    if sensor[3] == 0:
        persent = 0
    else:
        persent = round(sensor[3] * 100, 2)

    return render_template('sensor_emulator.html', id=id, percentage=persent, address=sensor[2], status=sensor[0], am_of=sensor[5])


@app_route.route('/')
def Hello_page():
    return render_template('hello_page.html')

