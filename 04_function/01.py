#Basic function syntax
#Write a function to calculate and return the square of the number 

def sqr(a):
    return a ** 2          #(a ** 2 -> a * a ). (a ** 3 -> a * a * a)

print(sqr(9));

# Create a function that takes two function as a parameter and return a sum

def sum(a , b):
    return a + b

print(sum(94,55))

# Polymorphism in functions

#Write a function multiply that multiplies two numbers, but can also accept and multiply strings.

def multiply(p1 , p2):
    return (p1 * p2)

print(multiply(8,9))
print(multiply('a', 5))
