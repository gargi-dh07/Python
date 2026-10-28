# Ask the user for a string and check whether it is a palindrome or not

s = input("Enter a string: ")

if (s == s[::-1]):
    print("It is a palindrome")
else:
    print("It is not a palindrome")

#Given a list of integers compute the average of all numbers in the list

list= [1,2,3,4,5]

sum=0
for i in list:
    sum+=i
print(sum)    
average= sum /len(list)
print(average)
