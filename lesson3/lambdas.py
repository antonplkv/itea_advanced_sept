
def func1(a):
    print("I am func1")
    print(f"my arg is {a}")

    def func2(b):
        print(f"I am func 2")
        print(f"My arg is {b}")

        def func3(c):
            print("Iam final func")
            print(f"And my arg is {c}")


        return func3
    return func2

func1(1)(2)(3)