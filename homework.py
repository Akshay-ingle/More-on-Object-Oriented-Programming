import math

class Circle:
    def __init__(self, radius):
        """Initialize the circle with a given radius."""
        self.radius = radius

    def area(self):
        """Calculate and return the area of the circle."""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Calculate and return the perimeter (circumference) of the circle."""
        return 2 * math.pi * self.radius

# Example usage:
radius = float(input("Enter the radius of the circle: "))
circle = Circle(radius)

print(f"Area: {circle.area():.2f}")
print(f"Perimeter: {circle.perimeter():.2f}")
