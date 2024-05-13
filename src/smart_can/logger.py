import pymongo
from datetime import datetime
import numpy as np
from itertools import islice
from pymongo import cursor

class Logger:
    def __init__(self, db_name):
        self.info = []
        self.client = pymongo.MongoClient('mongodb://localhost:27017/')
        self.db = self.client[db_name]

    def insert_data(self, sensors) -> None:
        result = {'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

        for id in sensors:
            result[str(id)] = {"fillment": sensors[id][3], "amount": sensors[id][5], "address": sensors[id][2]}
        
        return self.db["fillment"].insert_one(result)

    def read_data(self, collection, value={}, field={}) -> cursor:
        return self.db[collection].find(value, field)
    
    def get_mean_fill(self) -> float:
        last_object = self.db["fillment"].find().sort({"_id": -1})[0]
        sensors_fillment = []
        sensors = dict(islice(last_object.items(), 2, len(last_object)))

        for i in sensors:
            sensors_fillment.append(sensors[i]["fillment"])

        avg_fill = np.average(sensors_fillment)

        return avg_fill

    def get_last_added_object(self, collection) -> list:
        return self.db[collection].find().sort({"_id": -1})[0]

    def get_all_sensors(self) -> list:
        db_sensors = self.db["sensors"].find()
        sensors = []
        for sensor in db_sensors:
            sensors.append(sensor)
        return sensors

    def add_new_sensor(self, trash_type):
        template = {"STATUS": "FALSE", "TRASH_TYPE": trash_type, "COORDINATES": {"longitude": 59.9311 ,"latitude": 30.3609}, "PERCENTAGE": 0, "MAX": 100, "AMOUNT": 0}
        self.db["sensors"].insert_one(template)
        return self.get_last_added_object("sensors")

    def change_sensors_data(self, id: dict, args: dict) -> None:
        self.db["sensors"].update_one(id, args)