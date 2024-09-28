# Print the multiplication table for a given number up to 10 , but skipping 5th iteration

num = int(input("Enter the number : "))
mul = 1;

for i in range(10):
    if i == 5:
        continue
    else:
        mul = num * i;
        print(mul)