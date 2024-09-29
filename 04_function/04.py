# (*args)

# Function with (*args) : It allows you to handle multiple arguments without needing to define each one individually.

#Write a function that takes variable number of arguments and return their sum

def sum_all(*args):
    return sum(args)

result1 = sum_all(1, 2, 3, 4)
result2 = sum_all(1, 2, 3, 4 , 6 , 8 ,10)
print(result1)  # Output: 10
print(result2)