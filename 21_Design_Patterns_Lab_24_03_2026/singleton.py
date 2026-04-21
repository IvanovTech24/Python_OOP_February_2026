#with decorator
def singleton(cls):
    instance = [None]
    def wrapper(*args, **kwargs):
        if instance[0] is None:
            instance[0] = cls(*args, **kwargs)
        return instance[0]
    return wrapper

@singleton
class Singleton:
    def __init__(self):
        pass

s1 = Singleton()
s2 = Singleton()

print(s1 is s2)

print(s1)
print(s2)

print(id(s1))
print(id(s2))



# without decorator
class Singleton:
    __instance = None

    def __init__(self):
        if Singleton.__instance is not None:
            raise Exception("This is singleton")

    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

s1 = Singleton.get_instance()
s2 = Singleton.get_instance()

print(s1 is s2)

print(s1)
print(s2)

print(id(s1))
print(id(s2))
