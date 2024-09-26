# Strings are surronded by either "Hello" or by 'Hello'

st1 = "masala chai" 
first_char = st1[0]    # This is how you directly access any of the character present in the string.
print(first_char)

print(len(st1));      # To get the length of the string.

# If we want to get the character from 'any index' 'to any index' we can do slicing 

st2 = st1[3:7];
print("Here is the string from 3rd index to 7th index" , "'",st2,"'");

#Now will take a number string

st3 = "0123456789"
print(st3[:])      # Will print the whole string
print(st3[3:])     # will start from 3rd index till last index.
print(st3[:6])     # Will start from 0th index to the last index.

print(st3[0:10:3])  #Will return character from 0th index to 10th index but with the hop of 1 number (2nd number is not inclusive).


# There are lots of inbuilt methods in string.

print(st1.upper())
print(st1.lower())

# If there are lots of space in front and behind the string .

chai = '    cutting chai      ';
# .strip() : will return the string by removing all these white spaces from the beigning and ending.

print(chai.strip());

# Now if we want to replace any value from the string . 
print(chai.replace('cutting' , 'lemon')) ;     # Will replace 'cutting'  to 'lemon' from the string

greet = "Hey anshul do u want to have chai chai chai";

# ************* for Loop in python ************

for it in greet: 
    print(it);


print(greet.find("anshul"));       # Will check for 'anshul' if found will return the starting index , if not it returns -1
print(greet.count('chai'));        # Will print the count of the 'chai' in the string.

# Another important method. '.format()'
chai_type = "lemon"
quantity = 2
order = "I want {} cups of {} tea";    #I can allign variables inside these braces using '.format()' method 
print(order.format(quantity , chai_type));


# "  "space you need between string".join()". -: If we want to convert the list to string

chai_variety = ['Lemon' , 'Cutting' , 'Ginger']
print(" ".join(chai_variety));




