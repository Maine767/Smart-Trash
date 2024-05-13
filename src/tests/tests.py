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
Panel.new_chart(_logger)
Panel.new_prediction(_logger)