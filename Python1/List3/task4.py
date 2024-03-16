class Shape:
    def __init__(self,perimeter,area) :
           self.perimeter = perimeter
           self.area = area
class Circle(Shape):
        def calculate_perimeter_circle(self,radius):
               self.perimeter = 2*3.14*radius
               return self.perimeter
        def calculate_area_circle(self,radius):
               self.area = 3.14*radius*radius
               return self.area
class Square(Shape):
        def calculate_perimeter_square(self,length):
               self.perimeter = 4*length
               return self.perimeter
        def calculate_area_square(self,length):
               self.area = length*length
               return self.area

class Triangle(Shape):
        def calculate_perimeter_triangle(self,a,b,c):
               self.perimeter = a+b+c
               return self.perimeter
        def calculate_area_triangle(self,a,b,c):
               s = (a+b+c)/2
               self.area = (s*(s-a)*(s-b)*(s-c))**0.5
               return self.area
circle_1 = Circle(perimeter=0,area=0)
print("Area of a circle :" , circle_1.calculate_area_circle(5))
print("Perimeter of a circle :" , round(circle_1.calculate_perimeter_circle(5)))
Square_1 = Square(perimeter=0,area=0)
print("Area of a Square :" , Square_1.calculate_area_square(5))
print("Perimeter of a Square :" , Square_1.calculate_perimeter_square(5))
Triangle_1 = Triangle(perimeter=0,area=0)
print("Area of a Triangle :" , round(Triangle_1.calculate_area_triangle(5,5,5)))
print("Perimeter of a Triangle :" , Triangle_1.calculate_perimeter_triangle(5,5,5))




