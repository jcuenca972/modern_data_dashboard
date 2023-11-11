from pymongo import MongoClient

class AppModel:

    def __init__(self):
        self._client = MongoClient("mongodb://mbd_user:bigdata@154.56.46.126:27017/?authMechanism=DEFAULT")
        self._db = self._client["mbd_db"]
        self._collection = self._db["london_predictions"]

    def read_prediction(self, borough_option, vehicle_option,
                        month_option, day_option):
        query = {"$and": [{"borough": borough_option},
                          {"type": vehicle_option},
                          {"month": month_option},
                          {"day": day_option}]}
        return self._collection.find_one(query)["prediction"]