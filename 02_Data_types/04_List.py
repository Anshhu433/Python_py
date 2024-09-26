# List(follows the 0 base indexing just like array) are used to store the collection of data . It can be of any type (number , string etc)

tea_varity = ['Brown' , 'Black' , 'Oolong' , 'white']
print(tea_varity)
# can access any of the index
print(tea_varity[3]);

#Slicing is same as the string
print(tea_varity[1:3]);     # [startindex , lastindex]  'lastindex is exclusive'
print(tea_varity[:3]);
print(tea_varity[0:])


# If we want to replace the any of the value from the index.

print(tea_varity[1:2]);         # Here we need assign value in the array format only
tea_varity[1:2] = ['Lemon']     # Repacing('Black' with 'Masala)
print(tea_varity)

#If we want to replace more than one value at same time

tea_varity[0:3] = ['Green' , 'Black' , 'Cutting'];    #Reaplacing value at index (0,1,2) with the mentioned.
print(tea_varity);

# Loops

for item in tea_varity:
    print(item , end="-" )    #Means after printing every item put "-"
print("\n")

if 'Lemon' in tea_varity:
    print('I have the Lemon tea ')
else:
    print("sorry")

#Lets just append the 'Lemon' tea at the list.

tea_varity.append("Lemon")       # .append() is just to add the value at the last of the list.
print(tea_varity)

tea_varity.pop()          #No parameter needed to pop() . beacause pop will pop out the last elemet from the list.

tea_varity.remove("Green")      #want to remove from any of the index.

print(tea_varity);





