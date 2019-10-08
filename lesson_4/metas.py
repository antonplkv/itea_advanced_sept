a = tuple([1, 2])

print(type(int))

my_class = type(
    "ClassExample",
    (),
    {
        "attr_1": 100,
        "attr_2": 200,
        "get_attr_1": lambda self: self.attr_1,
        "get_attr_2": lambda self: self.attr_2,

    }
)
#
#
class MyMetaClass(type):

    def __new__(mcs, name, base, attrs):
        print(mcs, name, base, attrs)

        if attrs.get("CLASS_FIELD1", 0) < 100:
            attrs["CLASS_FIELD1"] = 1000

        if not attrs.get("verywellfield"):
            attrs["verywellfield"] = "my_value"


        return super().__new__(mcs, name, base, attrs)


class OurClass(metaclass=MyMetaClass):
    CLASS_FIELD1 = 101
    CLASS_FIELD2 = 2

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)

    def __init__(self, value):
        self._value = value




print(OurClass.CLASS_FIELD1)
#
from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def move(self):
        print("Moving!!!")

    def get_fuel(self):
        return self._fuel

class Car(Vehicle):

    def __init__(self, model, fuel=0):
        self._model = model
        self._fuel = fuel

    def move(self):
        super().move()



car = Car("BMW")
car.move()
print(car.get_fuel())
#
#
class PropertyExample:

    def __init__(self, arg1):
        self._x = arg1

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        if value == 100:
            raise ValueError()
        self._x = value

    @x.deleter
    def x(self):
        del self._x
    #
    def get_x(self):
        return self._x

    def set_x(self, value):
        self._x = value

    x = property(get_x, set_x)
#
#
obj = PropertyExample(10)
print(obj.x)
obj.x = 100
print(obj.x)
#
#
class DecoratorsExample:

    NUM = 0
    def __init__(self):
        self._value = 100

    @classmethod
    def increacse_num(cls, num):
        cls.NUM += num

    @classmethod
    def get_num(cls):
        return cls.NUM

    @classmethod
    def create_one_more(cls):
        return cls()

    @staticmethod
    def validate_phone():
        print("Useful logic")

    def set_phone(self, phone):

        self._phone = DecoratorsExample.validate_phone(phone)



DecoratorsExample.increacse_num(100)
print(DecoratorsExample.get_num())
DecoratorsExample.my_func()



class Singletone(type):
    instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.instance:
            cls.instance[cls] = super().__call__(*args, **kwargs)
            return cls.instance[cls]
        else:
            raise Exception("Already exists")


class MyClass(metaclass=Singletone):
    def __init__(self):
        self._x = 100

a = MyClass()
b = MyClass()




