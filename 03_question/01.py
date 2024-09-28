#Movie ticket price are based on age : Age > 18 price is $12 , for Age < 18 price is $8 , There will be extra discount 
# of $2 on wednesday


age = int(input("Enter the age : "))
day = input("Enter the day : ")

# price =12 if age > 18 else 8;

if age > 18:
    price = 12
else: 
    price=8;

if day == "Wednesday":
    price -= 2

print("The price for the ticket is : " , price)