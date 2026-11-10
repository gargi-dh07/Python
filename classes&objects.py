class student:
    subject="python"
    college="ABC"
    year="4th year"

stud1= student()
stud2= student()
print(stud1)
print(stud1.subject,stud1.college, stud1.year)
print(stud2)
print(stud2.subject,stud2.college, stud2.year)

#using init fuction (constructor function)

class teacher:
    def __init__(self):
        print("this is a constructor")

teacher1= teacher()
teacher2= teacher()
teacher3= teacher()

#to print different name for diffent students using init function

class student:
    def __init__(self, name, cgpa):
        self.name=name
        self.cgpa=cgpa

stud1= student("Gargi",9.9)
stud2= student("Aaditya",9.8)
stud3= student("Kanika",9.9)

print(stud1.name,",",  stud1.cgpa)
print(stud2.name,",",  stud2.cgpa)
print(stud3.name,",",  stud3.cgpa)

