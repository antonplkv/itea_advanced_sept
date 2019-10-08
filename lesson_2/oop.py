class Vehicle:

    NUM_OF_DOORS = 4
    FUEL_TYPE = "Gas"

    def move(self):
        print("Car drives")

    def set_fuel(self, value):
        self._fuel += value

    def get_fuel(self):
        return self._fuel

    def get_brand(self):
        return self._brand

    def set_brand(self, value):
        self._brand = value

    def get_engine(self):
        return self._engine

    def set_engine(self, value):
        self._engine = value

    def __str__(self):
        return f"Brand is {self._brand} and engine is {self._engine}"


class Car(Vehicle):

    def __init__(self, brand, engine):
        self._brand = brand
        self._engine = engine
        self._fuel = 0

    def move(self):
        print("Move about 100 km per hour")





car = Car('bmw', 'v8')
print(car.get_brand())
car.move()

print(car)


class Example:

    __slots__ = ("_name")

    def __init__(self, name):
        self._name = name


obj = Example("example objects")

obj._name = "new name"
obj._my_cool_var = 11


