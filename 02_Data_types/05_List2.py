#****************  .copy() Method         ***********************

# tea_varity_copy = tea_varity;  --> Here both will referring to the same object.
# But if we want to make the diffrent refrence for the same values in List .
# first one is. --> " Tea_variaty_copy = ['Black', 'Cutting', 'white']"

#Second one is   .copy() --> Method now we are making the different refrence in the memory of the same values

tea_varity = ['Brown' , 'Black' , 'Oolong' , 'white']

tea_varity_copy = tea_varity.copy();

#Now changes at 'tea_varity_copy' will not be reflected at 'tea_varity'

tea_varity_copy.append("Cutting with masala ")

print(tea_varity_copy);
print(tea_varity)



#**************    List Comprehension   **************

#[expression for item in iterable if condition]

#expression : The operation to generate elements of the new list.

#****** Basic **********

#Create a list of squares from 0-9

# range(10). -> (value from 0-10)

squr = [x**2  for x in range(10)]
print(squr)


#List Comprehension with condition

even = [y for y in range(10) if y%2==0]
print(even)


#Applying a function 

words = ['hindi' , 'english' , 'urdu']
word = [z.upper() for z in words]
print(word);