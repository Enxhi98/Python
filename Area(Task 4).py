#Given that radius is 2 and area is calculated as 12.5678, 
#use string format operators to print the values of the variables radius and area so that the output looks like this
#import math fucntion
import math
radius = int(input("Radius: "))
area = math.pi*(radius ** 2)
print("The area of the circle is: \t%.2f" %area)


#Given a rectangle with width as 2.5 cm and length as 5 cm, calculate the area of the rectangle
import math
width = float(input("Please enter the width of a rectangle: "))
length = float(input("Please enter the height of a rectangle: "))
#calculate the area
Area = width * height
print("\n Area of a Rectangle is: %.2f" %Area)


#Given a square with side as 7 cm, calculate its perimeter and area
import math
slength = int(input("Enter side length of square: "))
print("What is the perimeter of the square?")
perimeter = 4 * slength
print("Perimeter of square =", perimeter, "\n")
print("What is the area of the square?")
area = slength ** 2
print("The area of the square is", area, "\n")

        
