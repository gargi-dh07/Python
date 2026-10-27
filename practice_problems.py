# #Given a list of tuples with info(name,subject):

# #list all unique courses

info = {
    ("Alice", "Math"),
    ("Bob", "Science"),
    ("Alice", "Science"),
    ("Charlie", "Math"),
    ("Alice", "English"),
    ("Charlie", "English")
}
empty_set=set()
for name,course in info:
    empty_set.add(course)

print(empty_set)

                        #  or

empty_set=set()
for val in info:
    empty_set.add(val[1])
print(empty_set)

#list students enrolled in english

for name,course in info:
    if (course=="English"):
        print(name)

#create dictionary (student, set of courses)

student_courses= {}

for name, course in info:
    if (student_courses.get(name)==None):
        student_courses.update({name:set()})
        student_courses[name].add(course)
    else:
        student_courses[name].add(course)

print(student_courses)


