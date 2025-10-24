from homework_2 import Friend


class Venicle:
    def start(self):
        print("Venicle is starting")

class Car(Venicle):
    def start(self):
        super().start()
        print("Venicle is starting")


class ElectricCar(Venicle):
    def electro_car(self):
        print("Electric car starting")

class Tesla(Car, ElectricCar):
    def start(self):
        super ().start()
        print("Tesla ready")


tesla = Tesla()
tesla.start()

