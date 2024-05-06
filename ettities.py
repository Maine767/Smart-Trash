from logger import Logger
from ManageUnits import MainControlUnit

_logger = Logger('Log')

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

Panel.get_unit_id()
