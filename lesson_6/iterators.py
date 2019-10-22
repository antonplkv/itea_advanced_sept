
# class SimpleIterator:
#
#     def __init__(self, start, end, step):
#         self._start = start
#         self._end = end
#         self._step = step
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#
#         while self._start < self._end:
#             self._start += self._step
#             return self._start
#
#         raise StopIteration
#
#
# obj = SimpleIterator(0, 3, 1)
#
#
# print(obj.__next__())
#
# print(obj.__next__())
# print(obj.__next__())
# print(obj.__next__())





# def generator_func(start, end, step):
#
#     while start < end:
#         start += step
#         yield start
#
#
# generator_expression = (x ** 2 for x in range(100))
#
# obj = generator_func(0, 2, 1)
# obj_iterator = iter(obj)
# print(next(obj_iterator))
# print(next(obj_iterator))
# print(next(obj_iterator))


class Array:

    TYPES = (int, str, float)


    def __init__(self, size, default_value):
        self._array = [default_value] * size

    def __setitem__(self, key, value):

        if isinstance(value, Array.TYPES) and key <= len(self) - 1:
            self._array[key] = value
            return

        raise ValueError("Out of range")

    def __getitem__(self, item):
        if isinstance(item, int) and item <= len(self) - 1:
            return self._array[item]
        raise ValueError("Out of range")

    def __str__(self):
        return str(self._array)

    def __len__(self):
        return len(self._array)


array = Array(100, None)

array[0] = 12
print(array[0])
print(array)

array[99] = 1
print(array[99])

array[100] = 1

print(len(array))


class MyList:

    def __init__(self, *args):
        self.list = list(args)


