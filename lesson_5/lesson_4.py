class Exm:
    """
    Этот класс делает след : ....
    """
    def __init__(self, arg1, arg2):
        self._arg = arg1
        self._arg2 = arg2

    def __call__(self, *args, **kwargs):
        print(Exm.__doc__)

class Dec:

    def __init__(self, f):
        self.f = f

    def __call__(self, *args, **kwargs):
        print("Decoration started")
        self.f()
        print("Ended")


@Dec
def func():
    print("Hello world")

func()
