from flask import Flask, request, render_template, json
from ManageUnits import MainControlUnit

app = Flask(__name__, template_folder='template', static_folder="static")

Panel = MainControlUnit(1, "Бутылки")
Panel.add_new_sensor()
Panel.add_new_sensor()
Panel.add_new_sensor()

Panel.change_status(1, True)
Panel.change_status(2, True)
Panel.change_status(3, True)

Panel.set_max(1, 50)
Panel.set_max(2, 510)
Panel.set_max(3, 150)

Panel.set_address(1, "59.9311, 30.3609")
Panel.set_address(2, "59.9311, 30.3609")
Panel.set_address(3, "59.9311, 30.3609")

Panel.set_trash(1, 5)
Panel.set_trash(2, 15)
Panel.set_trash(3, 52)
Panel.set_trash(3, 52)

Panel.get_unit_id()

Panel2 = MainControlUnit(2, "Бумага")

Panel2.set_number_type(2.2)

Panel2.add_new_sensor()
Panel2.add_new_sensor()
Panel2.add_new_sensor()

Panel2.change_status(1, True)
Panel2.change_status(2, True)
Panel2.change_status(3, True)

Panel2.get_unit_id()

@app.route('/connect')
def connect():

    Panel.set_trash(int(request.args.get('id', '')),int(request.args.get("amount","")))

    return json.dumps({'Проблема': request.args.get('alert', ''), 'Координаты': request.args.get("coordinates", ''), 'Кол-во бутылок': request.args.get("+1", '')})

@app.route('/choose')
def choose():

    ids = list()

    for i in len(Panel.get_objects()):
        ids.append(i+1)

    return render_template('', ids=ids)

@app.route('/check_statistic')
def statistic():
    return render_template('')

@app.route('/<int:id>')
def interface(id):
    sensor = Panel.get_object(id)
    return render_template('sensor_emulator.html', id=id, percentage=round(sensor[3] * 100, 2), address=sensor[2], status=sensor[0], am_of=sensor[5])

@app.route('/')
def Hello_page():
    return render_template('hello_page.html')

if __name__ == '__main__':
    app.run()
