# Filename:  class_decorator_example.py
class MyDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("Before class-based decorator")
        result = self.func(*args, **kwargs)
        print("After class-based decorator")
        return result