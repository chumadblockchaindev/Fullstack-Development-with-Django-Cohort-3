print(__name__)

bikes = {}

def get_all_bikes():
    return bikes

class Bike:
    def add_bike(self, make, model, year):
        bike_id = len(bikes)
        bikes[bike_id] = {
            "make": make,
            "model": model,
            "year": year
        }
        return bikes['bike_id']
    
    def get_bike(self, bike_id):
        return bikes.get(bike_id, "Bike not found")
    
bike_manager = Bike()