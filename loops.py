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