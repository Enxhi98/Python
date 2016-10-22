#Give the circle's radius a value and calculate its area.
#import math fucntion
import math
radius = int(input("Radius: "))
area = math.pi*(radius ** 2)
print("The area of the circle is: \t%.2f" %area)


#Give the rectangle a width and length value, calculate the area of the rectangle.
import math
width = float(input("Please enter the width of a rectangle: "))
length = float(input("Please enter the height of a rectangle: "))
#calculate the area
Area = width * height
print("\n Area of a Rectangle is: %.2f" %Area)


#Give the side a value and calculate the square's perimeter and area.
import math
slength = int(input("Enter side length of square: "))
print("What is the perimeter of the square?")
perimeter = 4 * slength
print("Perimeter of square =", perimeter, "\n")
print("What is the area of the square?")
area = slength ** 2
print("The area of the square is", area, "\n")

        
