# Create a rucursive function to calculate the factorial of the function

def fact(num):
    if num == 0:
        return 1
    return num * fact(num-1)

print(fact(5))