tuple= (10,20,30,"aaditya","gargi")

print(tuple)
print(len(tuple))

tup= ("string")         #expressions
tup2= (2.3)
print(type(tup))
print(type(tup2))

                       #loops in tuple

for val in tuple:
    print(val)

tuple_1= (1,2,3,4,2,4,3,2,5)

sum=0
for val in tuple_1:
    sum+=val
print(sum)

#to find out the index of a value stored in tuple
print(tuple_1.index(2))

#to print the number of times a value is repeated in a tuple
print(tuple_1.count(2))