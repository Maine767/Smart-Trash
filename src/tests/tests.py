import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], "../smart_can"))
from ManageUnits import MainControlUnit
from logger import Logger

_logger = Logger('Log')
Panel = MainControlUnit(1, "bottles")

sensors = _logger.get_all_sensors()

Panel.load_sensors(sensors)

print(Panel._objects)
for i in Panel.get_objects():
    print(i)
    sensor = Panel.get_object(i)
    print(sensor)
    persent = round(sensor[3] * 100 ) if sensor[3] > 0 else 0
    print(persent)