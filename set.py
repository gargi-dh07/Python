#immutable values are stored in the sets
#sets are mutable
#duplicate values can't be stored in sets


set_1= {11,2,34,2,2,2}       
                          
print(type(set_1))

#to write an empty set

empty_set= set()
print(type(empty_set))


                            #set methods

#to add a new value to the exisitng set
set_1.add(5)
print(set_1)

# #to remove a value form the set 
# set_1.remove(5)
# print(set_1)

# #to empy a set completely
# set_1.clear()
# print(set_1)

# #to remove a random value from the set
# set_1.pop()
# print(set_1)

# TO DO UNION AND INTERSECTION OF TWO SETS

s1= {1,2,3,4,5,6}
s2={4,5,6,7,8,9}

#PRINTING UNION
print(s1.union(s2))

#PRINTING INTERSECTION
print(s1.intersection(s2))