#Arithmatic operators
a=12
b=3

print(a+b)   #addition
print(a-b)   #subtraction
print(a/b)   #division
print(a*b)   #multiplication
print(a%b)   #modulo (used to calculate remainder)
print(a**b)  #prints a^b (a to the power b)

#relational operators 
c=10
d=5

print(c==d)
print(c>d)
print(c<d)
print(c!=d)
print(c>=d)

#Assignment operators
e=10
e+=1         #e=e+1
print(e)
e-=1         #e=e-1
print(e)
e*=2         #e=e*2
print(e)

#logical operators

# truth table of "or"

print("true or false is", True or False)    #True
print("true or true is", True or False)     #True   
print("false or True is", False or True)    #True
print("false or false is", False or False)  #False
print()
# Truth table of "and"

print("true and true is", True and True)      #True
print("false and true is", False and True)    #False
print("false and false is", False and False)  #False
print("true and False is", True and False)    #False
print()

#"not" operator 
#gives the opposite of the output

var_=False
Var_1= (5<8)

print(not(var_))      #gives True
print(not(Var_1))     #gives False