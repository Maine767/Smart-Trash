from flask import Flask, request, render_template, json
from manage_units import MainControlUnit

app = Flask(__name__, template_folder='template', static_folder="static")

Bottle_trash_1 = MainControlUnit(1, True, 0, "59.9311, 30.3609", 0)
Bottle_trash_2 = MainControlUnit(2, False, 0, "59.9311, 30.3609", 0)
Paper_trash_1 = MainControlUnit(3, True, 0, "59.9311, 30.3609", 0)
Paper_trash_2 = MainControlUnit(4, True, 0, "59.9311, 30.3609", 0)


if __name__ == '__main__':


    @app.route('/connect')
    def connect():

        print(request.args.get("alert",""))
        print(request.args.get("coordinates",""))

        old_count_of_bottles = Bottle_trash_1.get_trash()
        #Bottle_trash_1.bottle_count += int(request.args.get("+1",""))

        print(Bottle_trash_1.get_trash())

        #Bottle_trash_1.fill_percentage = round(Bottle_trash_1.bottle_count*Bottle_trash_1.fill_percentage/old_count_of_bottles)
        
        return json.dumps({'Проблема': request.args.get('alert', ''), 'Координаты': request.args.get("coordinates", ''), 'Кол-во бутылок': request.args.get("+1", '')})


    @app.route('/interface')
    def interface(value):
        print(value)
        return {}

    @app.route('/new_value/<value>')
    def save_value(value):
        print(value)
        return {}


    @app.route('/sensor/<int:temp>')
    def show_sensor(temp):
        save_value(temp)
        return f'текущее значение: {temp}'


    @app.route('/')
    def simulate_trash():
        address = Bottle_trash_1.get_address()
        full = Bottle_trash_1.get_fill_percentage()
        count_of_bottles = Bottle_trash_1.get_trash()
        return render_template('sensor_emulator.html', full=full,count_of_bottles=count_of_bottles)


    if __name__ == '__main__':
        app.run()
