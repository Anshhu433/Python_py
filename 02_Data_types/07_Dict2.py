# Nested dictionaries
# {{} , {} , {}}

tea_shop = {
    'chai' : {'masala' : 'spicy' , 'ginger' : 'zesty'}, 
    'tea' : {'cutting' : 'sweet' , 'green' : 'fresh'}
}


# chai is the key with values {'masala' : 'spicy' , 'ginger' : 'zesty'} and then 'masala' and 'ginger' are the keys with values
# 'spicy' and 'zesty

# Lets see how we can the values from nested dictionaries.

print(tea_shop['chai'])       #Here we will get the values inside the 'chai' key
print(tea_shop['chai']['masala'])       # Here we will get the value inside the 'masala' key.

#simi with 'tea'

print(tea_shop['tea'])
print(tea_shop['tea']['cutting'])  


# ********** Dict comprehension **************


squr = {x:x**2 for x in range(10)}
print(squr);


# If we want to convert list to dict.
# dict.fromkeys(keys , default_value)

keys = ['cutting' , 'ginger' , 'masala']
default_value = 'Delicious'
new_dict = dict.fromkeys(keys , default_value);
print(new_dict);
 