#define and call a function

def hello():
    print("hello world \nThis is GARGI")
hello()

#function definition 
def sum(a,b):    #parameters
    s=a+b
    return s

#calling the function 
ans=sum(4,5)
print(sum(4,5))
print(ans)

#calc average of three numbers

def calc_avg(a,b,c):
    average=(a+b+c)/3
    return average
print(calc_avg(2,2,2)) 

#assigning defalt values 

def sum(a,b=1):
    return a+b
print(sum(4))

#USING LAMBDA FUNCION

sum= lambda a,b: a+b
print(sum(4,5))

avg= lambda a,b: (a+b)/2
print(avg(2,4))

#WRITE A CODE TO PRINT THE FACTORIAL OF A NUMBER 'n'

def calc_factorial(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact

n=int(input("ENTER YOUR NUMBER:"))
print(calc_factorial(n))
    

