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

# Panel2 = MainControlUnit(2, "Бумага")
# Panel2.add_new_sensor()
# Panel2.add_new_sensor()
# Panel2.add_new_sensor()

# Panel2.change_status(1, True)
# Panel2.change_status(2, True)
# Panel2.change_status(3, True)

if __name__ == "__main__":

    @app.route('/connect')
    def something():
        None