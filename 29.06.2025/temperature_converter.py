# Filename: temperature_converter.py
class TemperatureConverter:
    def __init__(self, celsius=None, fahrenheit=None):
        self.celsius = celsius
        self.fahrenheit = fahrenheit

    def convert_celsius_to_fahrenheit(self):
        if self.celsius is not None:
            return (self.celsius * 9/5) + 32
        return None

    def convert_fahrenheit_to_celsius(self):
        if self.fahrenheit is not None:
            return (self.fahrenheit - 32) * 5/9
        return None