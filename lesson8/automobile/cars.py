cars = {}

class Car:
    def add_car(self, make, model, year):
        car_id = len(cars)
        cars[car_id] = {
            "make": make,
            "model": model,
            "year": year
        }
        return cars[car_id]
    
    def get_car(self, car_id):
        return cars.get(car_id, "Car not found")
    
car_manager = Car()


if __name__ == "automobile.cars":
    print(car_manager.add_car("Toyota", "Camry", 2020))
    car_manager.add_car("Honda", "Civic", 2019)
    print(car_manager.add_car("Ford", "Mustang", 2021))
    car_manager.add_car("Chevrolet", "Malibu", 2018)

    print(car_manager.get_car(1))

    print(cars)