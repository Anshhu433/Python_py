#Compute the factorial of the given number 

# n = int(input('Enter the number ; '))
# fact = 1
# for i in range(1, n+1):
#     fact = fact * i

# print(fact)


number  = 5
fact = 1

while number>0:
    fact = fact * number
    number = number - 1

print(fact);