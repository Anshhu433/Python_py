# Loops in python

#Counting Positive Number 
#Given a number of list count how many are positive

num = [1,2,-2,-3,4,6,7]

count = 0;
for i in num:
     if i > 0:
          print(i)
          count+=1
     else:
          continue
     
print("The count of the positive number is ; " , count);