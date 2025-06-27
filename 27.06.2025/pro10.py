def log_methods(cls):
    for attr in cls.__dict__:
        if callable(getattr(cls, attr)):
            orig = getattr(cls, attr)
            def wrapper(*args, **kwargs):
                print(f"Calling {orig.__name__}")
                return orig(*args, **kwargs)
            setattr(cls, attr, wrapper)
    return cls

@log_methods
class Test:
    def add(self, x, y):
        return x + y

t = Test()
print(t.add(3, 4))
