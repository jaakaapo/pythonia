def my_decorator(func):
    def wrapper():
        print("Line 1")
        func()
        print("Line 2")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

#say_hello = my_decorator(say_hello)

say_hello()