a=5
b=10
sum=a+b

#NORMAL FORMATTING

print("THE SUM OF THE TWO NUMBERS IS {}".format(sum))
print("THE SUM OF {} AND {} IS {}".format(a,b,sum))

#INDEX BASED FORMATTING

print("THE SUM OF {1} AND {0} IS {2}".format(a,b,sum))

#VALUE BASED FORMATTING

print("THE TWO VARIABLES ARE {a} AND {b}".format(a=10,b=15))

# f STRINGS

c=10
d=15

print(f"THE SUM OF {c} AND {d} IS {c+d}")
print(f"AVERAGE OF {c} AND {d} IS {(c+d)/2}")