                               #WHILE LOOPS
#Infinte loop

while True:
    print("hello world")

# # Finite loop =>5x

count=1 #iterator
while (count<=5):
    print("hello world")
    count+=1
print("After loop count:",count)

# #print no. from 1-10 using loop

i=0
while (i<11):
    print(i)
    i+=1

# #reverse loop

i=10
while(i>=1):
    print(i)
    i-=1

#print multilication table of any no. '5'

n=int(input("ENTER THE NO.:"))
i=1
while(i<=10):
    print(i*n)
    i+=1

#BREAK 

i=1
while (i<=10):
    if (i%6==0):
        break
    print(i)
    i+=1

#CONTINUE

i=1
while(i<=10):
    if(i%3==0):
        i+=1
        continue
    print(i)
    i+=1
print("loop exited")

# PRINT ALL THE ODD NO. FROM 1 TO 10 
# USING CONTINUE

i=0

while (i<10):
    i+=1
    if (i%2==0):
        continue
    print(i)
print("these are all the odd numbers from 1 to 10")

#without using CONTINUE

i=1
while(i<=10):
    print (i)
    i+=2
print("THESE ARE ALL THE ODD NUMBER FROM 1 TO 10")

                                 #fOR LOOPS

string="hello"

#in=> membership operator (used to check the presence)
for var in string:
    print(var)

#PRINT HELLO WORLD 5 TIMES

for i in range(5):
    print("HELLO WORLD")

#COUNT THE NO ID i's IN THE STRING
string="Artificial Intelligence"

count=0
for letter in string:
    if (letter=='i'):
        count+=1
print("THE NO. OF i's in string are :",count)

#PRINT THE NO. OF VOWELS PRESENT IN THE GIVEN STRING 

name= "Gargi Dhiman"
count=0
for i in name:
    if (i=='a'or i=='e'or i=='i'or i=='o'or i=='u'):
        count+=1
print("NO. OF TOTAL VOWELS IN THE STRING 'NAME' ARE:",count)

#RANGE FUNCTION IN LOOPS
#used to generate sequence       =>         range(start,stop, step)
print("1. Print no from 0 to 5")   
for i in range(6):                          #by default the stating point is 0
    print(i)

print("2. Print no. from 1-5")
for i in range(1,6):                        # for i in range(a,b-1)
    print(i)

print("3. Print n. from 1 to 10 with a stepping of 1 numbers")
for i in range(1,10,2):
    print(i)

#PRINT THE SUM OF FIRST 10 NATURAL NUMBERS

n= int(input("ENTER A NUMBER :"))
sum=0
for i in range(1,n+1):
    sum+=i
print("SUM:",sum)