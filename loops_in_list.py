#using for loops in list

list= [10,20,30,40,50]

x=50
index=0

for val in list:
    if (val==x):
        print(f"x found at index:{index}")
        break
    index+=1
