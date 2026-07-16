from functools import wraps


def my_decorator(fun):
    @wraps(fun())
    def wrapper(*args, **kwargs):
        print("Before the function execution...")
        result = fun(*args, **kwargs)
        print("After the functions execution...")
        return result

    return wrapper


@my_decorator
def greet():
    print("Hello world from the decorator")


@my_decorator
def calculation(x, y):
    return x + y


greet()
result = calculation(4, 8)
print(result)
print(calculation.__name__)
