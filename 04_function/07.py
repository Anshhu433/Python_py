#Generator function with yeild


#write a generator function that yeilds the even numbers upto a specified limit 

# def even(limit):
#     for i in range(2 , limit+1 , 2):
#         return i

# for num in even(10):
#     print(num);           #Here '2' will be printed always. because Once return is used, the function's execution is over, 
                          #and it cannot resume from where it left off.



# yeild :  yield is used in a function to return a value and pause the function's execution, allowing it to resume later 
# from where it left off.

# Now we will create the function using yeild

def even(limit):
    for i in range(2 , limit+1 , 2):
        yield i

for num in even(10):
   print(num);