# Function with (**kwargs)
#In Python, **kwargs allows a function to accept an arbitrary number of keyword arguments (arguments passed as key-value pairs). 
#These keyword arguments are packed into a dictionary inside the function

#Create a function that accepts any number of keyword arguments and prints them in the format of  key:value

def print_kwargs(**kwargs):
    for key , value in kwargs.items():
        print(f"{key} : {value}")


print_kwargs(name= 'Anshul' , power = 'lazer')
print_kwargs(name = 'Anshika' )
print_kwargs(name = 'Liza' , power = 'Cuteness' , last_name = 'sharma')