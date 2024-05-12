from flask import render_template, request, json, Blueprint
from tests import _logger, Panel

app_route = Blueprint('route', __name__)


@app_route.route('/connect')
def connect():

    print(Panel.new_charts(_logger))

    try:
        id = int(request.args.get('sensor_id', ''))
        amount = int(request.args.get("amount",""))
        Panel.set_trash(id, amount)
    except ValueError:
        print("Value/Values are incorrect")

    _logger.insert_data(Panel.get_objects())

    return json.dumps({'id': request.args.get('sensor_id', ''),"percentage": request.args.get("percentage", ""),"address": request.args.get("address", ""), 'status': request.args.get('status', ''), 'Кол-во бутылок': request.args.get("amount_of", '')})


@app_route.route('/selection_panel')
def choose():
    ids = list()
    for i in Panel.get_objects():
        ids.append(i)
    return render_template('selection_panel.html', ids=ids)


@app_route.route('/settings/sensor/<sensor_id>')
def set_setting(sensor_id):
    sensor = Panel.get_object(sensor_id)
    persent = round(sensor[3] * 100 ) if sensor[3] > 0 else 0
    print("IMHERE")
    return render_template("settings.html", sensor_id=sensor_id, percentage=persent, address=sensor[2], status=sensor[0], amount_of=sensor[5])


@app_route.route('/create_new_sensor')
def create_new_sensor():
    sensor_id = Panel.add_new_sensor()
    sensor = Panel.get_object(sensor_id)
    return render_template('settings.html', id=sensor_id, percentage=0, address=sensor[2], status=sensor[0], am_of=sensor[5])

@app_route.route('/profile')
def profile():
    mean_fillment = _logger.get_mean_fill()

    sensors = Panel.get_objects()

    count = 0
    for i in sensors:
        if sensors[i][0] == True:
            count += 1

    return render_template('Profile.html', id_panel=Panel.get_unit_id(), sensors=len(sensors), active_sensors=count, mean_fill=mean_fillment)

@app_route.route('/')
def Hello_page():
    return render_template('start_page.html')

