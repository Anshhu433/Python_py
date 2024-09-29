# Function returning multiple values
# Create a function that returns both the area and circumference of a circle given its radius 

import math

def circle_stat(r):
    area = math.pi * r * r
    circum = 2 * math.pi * r
    return area, circum

a , c = circle_stat(5)

print('Area of the circel is : ' , a, '\n','Circumference of the circle is ; ', c );


#Default parameter value 
#Write a function that greet the user . If no name is provided , it should greet with a default name.

def greet(name = "Anshul"):      #This is the default value if no name is provided then this "Anshul" will be printed.
      print("hey " , name)

greet("Pinu")
greet()