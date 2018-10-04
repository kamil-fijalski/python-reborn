# Classes & Methods


class Circle(object):
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color

    def calc_diameter(self):
        return self.radius * 2

    def increasing_radius(self, r):
        self.radius = self.radius + r


class Rectangle(object):
    def __init__(self, height, weight, color):
        self.height = height
        self.weight = weight
        self.color = color


FirstCircle = Circle(10, "red")
SecondCircle = Circle(50, "blue")
SecondCircle.color = "green"

FirstRectangle = Rectangle(10, 20, "yellow")

print("Diameter of FirstCircle: " + str(FirstCircle.calc_diameter()))

str1 = "Radius of C1: " + str(FirstCircle.radius)
FirstCircle.increasing_radius(15)
print(str1 + " and after increasing is " + str(FirstCircle.radius))
