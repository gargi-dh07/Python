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

tuple_1= (1,2,3,4,5)

sum=0
for val in tuple_1:
    sum+=val

print(f"SUM OF VALUES IS :{sum}")