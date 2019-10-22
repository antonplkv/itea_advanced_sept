
file = open("file.txt", "w")
file.write("str")
file.close()

with open("file.txt", 'w') as file:
    file.write("str")


class ContextManagerExample:

    def __init__(self, a):
        self._a = a
        self._state = "Active"

    def __enter__(self):
        print("Context manager entered")
        return (self, 1)

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exit context")
        self._state = "Inactive"

    def process(self):
        print("Processing data")

obj = ContextManagerExample(10)

print(obj._state)
obj.process()

with ContextManagerExample(10) as new_obj:
    print(new_obj)
    new_obj[0].process()

print(new_obj._state)


