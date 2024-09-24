# How the refrencing works in mutable(List , Touple , Dict.) and in immutable(Number , String) Data types

a = 5;
c = 5;      #(here in immutabale Datatypes if variable having the same value they are pointing to the same object in memopry)
            # Here is the example.

print('Is Value of the both are same ' , a==c);
print('Both are pointing to same objects ', a is c);


b  = a;
a = a+2;
print(a);   #Here now what happens is 'a' is variable refrencing to a object inside the memory . In python Object has the data
            # data type not the variable so '5' is immutable (Number datatype) . 'a' starts refrencing to another object '5+2=7'
            # '5' will be collect/delete by the garbage collector from memory
            # Diagram demontration in notebook.

print(b);   # Question here is where will be 'b' pointing . 'b' will be pointing to '5'
            
            # Objects inside the variable are immutable . You cant change the object(number datatype) inside the variable. like in 
            # list, touple


# Lets take the example of the List (mutable datatype)

# In case of list , If two variables are pointing to same value then also they will point to 2 differ-differ objects
#Below is the Example
#Diagram demontration is in notebook

l1 = [1,2,3];
l2 = l1;
l3 = [1,2,3];

print(l1==l2);  # Same value or not -->True
print(l1 is l2);    # Same objects or not. --> True

print(l1==l3) ;   # --> True
print(l1 is l3);   # -->False. (beacuse even they have same value but they are not poiting to the same object).


l1[0]=33

print(l1);
print(l2);
print(l3);     #Value of l3 remains same even l3 contains the same object. because of the above reason(both variable l1 & l2
               # are refrencing to differ-differ objects.)

