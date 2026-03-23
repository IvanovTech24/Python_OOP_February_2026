def type_check(parameter):
    def decorator(func):
        def wrapper(*args):
            if isinstance(*args, parameter):
                return func(*args)
            return "Bad Type"
        return wrapper
    return decorator



@type_check(int)
def times2(num):
    return num*2
print(times2(2))
print(times2('Not A Number'))
