#Generator function with yeild


#write a generator function that yeilds the even numbers upto a specified limit 

def even(limit):
    for i in range(2 , limit+1 , 2):
        print(i)

even(10);