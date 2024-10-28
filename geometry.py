import math

def rectangle_area(base, height) :
    return base * height

def rectangle_perimeter(base, height) :
    return 2 * (base + height)

def square_area(side) :
    return side * side

def square_perimeter(side) :
    return 4 * side

def circle_area(radius) :
    return math.tau * (radius ** 2) / 2

def circle_circumference(radius) :
    return math.tau * radius
