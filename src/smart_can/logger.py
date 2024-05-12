import pymongo
from datetime import datetime
import numpy as np
from itertools import islice

class Logger:
    def __init__(self, db_name):
        self.info = []
        self.client = pymongo.MongoClient('mongodb://localhost:27017/')
        self.db = self.client[db_name]

    def insert_data(self, sensors):
        result = {'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

        for id in sensors:
            result[str(id)] = {"fillment": sensors[id][3], "amount": sensors[id][5], "address": sensors[id][2]}
        
        return self.db["fillment"].insert_one(result)

    def read_data(self, collection, value={}, field={}):
        return self.db[collection].find(value, field)
    
    def get_mean_fill(self):
        last_object = self.db["fillment"].find().sort({"_id": -1})[0]
        sensors_fillment = []
        sensors = dict(islice(last_object.items(), 2, len(last_object)))

        for i in sensors:
            sensors_fillment.append(sensors[i]["fillment"])

        avg_fill = np.average(sensors_fillment)

        return avg_fill

    def get_last_added_object(self, collection):
        return self.db[collection].find().sort({"_id": -1})[0]

    def get_all_sensors(self):
        db_sensors = self.db["sensors"].find()
        sensors = []
        for sensor in db_sensors:
            sensors.append(sensor)
        return sensors

    def add_new_sensor(self):
        self.db["sensors"].find()
        pass

    def change_sensors_data(self, id: int, status: bool, trash_type: str, place: str, per_fillment: int, max_fillment: int ,fillment: int):
        print(self.db["sensors"].find({"STATUS": "TRUE"}))
        for i in self.db["sensors"].find({"STATUS": "TRUE"}):
            print("h")
            print(i)
        pass