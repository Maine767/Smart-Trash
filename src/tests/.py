import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], "../smart_can"))
from logger import Logger
from ManageUnits import MainControlUnit

_logger = Logger('Log')
Panel = MainControlUnit(1, "Бутылки")

sensors = _logger.get_all_sensors()

Panel.load_sensors(sensors)
for i in Panel.get_objects():

    _logger.change_sensors_data(i, 0, 0, 0, 0, 0, 0)
    sensor = Panel.get_object(i)
    persent = round(sensor[3] * 100 ) if sensor[3] > 0 else 0
