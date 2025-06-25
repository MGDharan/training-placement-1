# Filename:  shape_calculator.py
import math

def circle_area(radius):
    return math.pi * radius**2

def rectangle_area(length, width):
    return length * width

def triangle_area(base, height):
    return 0.5 * base * height

radius = 5
length = 10
width = 5
base = 4
height = 6

print(f"Circle area: {circle_area(radius)}")
print(f"Rectangle area: {rectangle_area(length, width)}")
print(f"Triangle area: {triangle_area(base, height)}")