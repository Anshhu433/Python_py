# Sum of the even number 

# number = [ 1,2,3,4,5,6,7,8]

# sum = 0

# for i in number:
#     if i % 2 == 0:
#         sum = sum + i;
#     else:
#         continue

# print("The sum of the even number : " , sum)

n = 10;
sum = 0;

for i in range(1 , n+1):        # range(from , till(exclusive))
    if i%2 == 0:
        sum += i
    
print("Sum of the even number is : " , sum);
