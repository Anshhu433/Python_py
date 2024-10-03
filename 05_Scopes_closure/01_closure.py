
#closure : a closure is a function that "remembers" variables from the surrounding scope where it was created, 
#even after that scope has finished execution.

def coder(num):
    def actual(x):               #actual(inner function) is using the number from the coder(outer function).
        return x ** num
    return actual

result = coder(2)     # coder() this function is returning a function that is stored in result.
print(result(4))      # Now as we know 'actual' is stored inside 'result' so we are calling 'result

# One more example

def outer_func(name):
    def inner_func(x):
        print(f'Hey {name} your performance is {x} out of 5')   #Inner function is using the name from the outer function
    return inner_func        # Returning the inner_func

my_closure = outer_func('Anshul')
my_closure(4);
