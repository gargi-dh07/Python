# # Ask the user for a string and check whether it is a palindrome or not

# s = input("Enter a string: ")

# if (s == s[::-1]):
#     print("It is a palindrome")
# else:
#     print("It is not a palindrome")

# #Given a list of integers compute the average of all numbers in the list

# list= [1,2,3,4,5]

# sum=0
# for i in list:
#     sum+=i
# print(sum)    
# average= sum /len(list)
# print(average)


def print_even(a, b):
    for i in range(a, b + 1):
        if i % 2 == 0:
            print(i)

num1 = int(input("Enter first integer: "))
num2 = int(input("Enter second integer: "))

print_even(num1, num2)