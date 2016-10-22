"""Given that radius is 2 and area is calculated as 12.5678, 
use string format operators to print the values of the variables radius and area so that the output looks like this"""
#import math fucntion
import math
radius = int(input("Radius: "))
area = math.pi*(radius ** 2)
print("The area of the circle is: \t%.2f" %area)
