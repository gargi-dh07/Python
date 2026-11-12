# Write a program that takes a string from the user and prints the number of spaces in the string.

string = input("Enter a string: ")

count = 0

for i in string:
    if i == " ":
        count += 1

print("Number of spaces in the string:", count)

# Input two lists of integers from the user. Merge them into one list and sort the result.

list1 = []
list2 = []

n1 = int(input("Enter the number of elements in first list: "))

for i in range(n1):
    num = int(input("Enter a number: "))
    list1.append(num)

n2 = int(input("Enter the number of elements in second list: "))

for i in range(n2):
    num = int(input("Enter a number: "))
    list2.append(num)

# Merging both lists
result = list1 + list2

# Sorting the merged list
result.sort()

print("Merged and sorted list:", result)
