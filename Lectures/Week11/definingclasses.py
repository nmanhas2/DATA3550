class Circle:
  pi = 3.1415926
  def __init__(self, radius) :
    self.radius = radius

  def area(self) :
    return self.radius * self.radius * self.pi

my_circle = Circle(5)
my_circle.pi = 1
print(my_circle.area())