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

#calc average

def calc_avg(a,b,c):
    sum=a+b+c
    return sum/3
print(calc_avg(5,10,15))