def my_decorator_with_params(arg1, arg2):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print("Start decorator")
            print(f"Decorator params: {arg1}, {arg2}")
            result = func(*args, **kwargs)
            print("End decorator")
            return result
        return wrapper
    return decorator


@my_decorator_with_params("arg1", "arg2")
def my_func():
    print("Test")

my_func()