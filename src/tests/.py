import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], "../smart_can"))
from logger import Logger
from ManageUnits import MainControlUnit
from bson.objectid import ObjectId

_logger = Logger('Log')
Panel = MainControlUnit(1, "bottles")

cursor = _logger.get_all_sensors()
Panel.load_sensors(cursor)

characteristics = dict()

for i in Panel.get_objects():

    cursor = _logger.read_data('sensors', {'_id': i})
    for j in cursor:
        for k in j:
            characteristics[k] =  j[k]

    characteristics["MAX"] = 100
    print(characteristics)
    _logger.change_sensors_data({"_id": characteristics["_id"]}, {"$set": characteristics})
    
    sensor = Panel.get_object(i)
    persent = round(sensor[3] * 100 ) if sensor[3] > 0 else 0
