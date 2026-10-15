# #ques 1.Write a program that asks the user for their name and age, then prints a sentence

name=input("enter your name:")
age=input("enter your age:")
print(f"Hello {name}!, your age is {age}")

# #ques2.Take two numbers as input from the user and print their sum,difference, product and quotient

a=int(input("enter the first no.:"))
b=int(input("enter the second no.:"))

sum=a+b
diff=a-b
multi=a*b
quo=a//b

print("SUM OF THE TWO NO. IS:", sum)
print("DIFFERENCE OF THE TWO NO. IS:", diff)
print("PRODCUT OF THE TWO NO. IS:", multi)
print("QUOTIENT OF THE TWO NO. IS:", quo)

#ques3. Ask the user to enter two integers and one float. Convert them all to floats and print their average.

num_1=int(input("ENTER AN INTEGER VALUE"))
num_2=int(input("ENTER AN INTERGER VALUE"))
num_3=float(input("ENTER A DECIMAL VALUE"))

num_1= float(num_1)
num_2=float(num_2)
print(num_1, type(num_1))
print(num_2, type(num_2))
print("AVERAGE OF THE THREE NUMBERS IS: ", (num_1+num_2+num_3)/3)