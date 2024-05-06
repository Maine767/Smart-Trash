import pymongo
from datetime import datetime

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
    
    def last_added_element(self, collection, field):
        self.db[collection].find().sort({field: -1}).limit(1)