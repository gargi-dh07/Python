age=int(input("enter your age:"))

if age>=18:
    print("you can vote")
else:
    print("you can't vote")

# USING if, elif,and else determine the signal_

color=input("enter the color:")

if color=="red":
    print("stop")
elif color=="yellow":
    print("look")
elif color=="green":
    print("go")

#Print the category of crowd based on their age

age=int(input("ENTER YOUR AGE:"))

if age<13:
    print("The candidate is a CHILD")
elif age>=13 and age<=19:
    print("The candidate is a TEENAGER")
elif age>19:
    print("The candidate is an ADULT")

# #USERNAME AND PASSWORD

username= input("ENTER YOUR USERNAME")
password= input("ENTER THE PASSWORD")

if (username=="ADMIN" and password=="1234"):
    print("LOGIN SUCCESSFUL!")
elif (username!= "ADMIN"):
    print("wrong username!")
else:
    print("password is wrong")


# #DETERMINE IF THE NO. IS EVEN OR ODD

num= int(input("ENTER A NUMBER"))

if (num%2==0):
    print("NO. IS EVEN")
else:
    print("NO. IS ODD")


# #USERNAME AND PASSWORD through NESTING

username= input("ENTER YOUR USERNAME")
password= input("ENTER THE PASSWORD")

if (username=="ADMIN" and password=="1234"):
    print("LOGIN SUCCESSFUL!")
else:
    if (username!="ADMIN"):
        print("worng username")
    else:
        print("wrong password")


color=input("ENTER A COLOR")

match color:
    case "green":
        print("go")
    case "red":
        print("stop")
    case "yellow":
        print("look")
    case _:
        print("worng color")