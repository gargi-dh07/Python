list=[10,20,30,40,50,60]

print(list)                             #printing elements of the list
print(len(list))                        #printing the length of the list
print(list[2])                          #printing values thorugh indexing

list[2]=56                              #assigning new value
print(list)

print(type(list))                       #printing the type

#SLICING

print(list[:5])
print(list[5:])
print(list[-5:-2])

#USING SOME OPERATIONS ON LIST

nums= [1,2,3]

nums.append(4)                    #add a value to the end of the list
print(nums)                       
                          
nums.insert(2,10)                 #add the value at a specific index
print(nums)

nums.sort()                       #sort the values
print(nums)

nums.reverse()                    #reverse the values
print(nums)

    #or

nums.sort(reverse=True)
print(nums)