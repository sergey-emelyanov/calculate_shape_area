from calc_area import Circle, Triangle


def print_area(shape):
    print(f"Area: {shape.area()}")


circle = Circle(30)
print_area(circle)
triangle = Triangle(3, 4, 5)
print_area(triangle)
