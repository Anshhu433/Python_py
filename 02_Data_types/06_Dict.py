# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

chai_types = {
    'masala' : 'spicy',
    'ginger' : 'zesty',
    'green' : 'fresh'
}

print(chai_types);
print(chai_types['ginger'])     #Want to get the value from the key

#loop to get only the value from the keys

for types in chai_types:
    print(chai_types[types])

#loop to get key and value both but not in the dict. format

for item in chai_types:
    print(item , chai_types[item])

#If want to add another key:value pair in the existing list

chai_types["Cutting"] = 'Sweet'
print(chai_types);

#Here if want to delete any item from the dict. we use .pop()
# Here .pop("key")  here pop needs parameter to delete the whole item
# another method '.popitem()' which do not require any parameter bcz it pop out the last element from the dict.

chai_types.pop('ginger');
print(chai_types);

chai_types.popitem();
print(chai_types);

