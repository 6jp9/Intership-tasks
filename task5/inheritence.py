# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def display(self):
#         print(self.name,self.age,end=' ')
# class Student(Person):
#     def __init__(self,name,age,roll,grades):
#         super().__init__(name,age)
#         self.roll=roll
#         self.grades=grades
#     def display(self):
#         super().display()
#         print(self.roll,self.grades, end=' ')

# class GraduateStudent(Student):
#     def __init__(self,name,age,roll,grades,degree):
#         super().__init__(name,age,roll,grades)
#         self.degree=degree
#     def display(self):
#         super().display()
#         print(self.degree)
    
# person = Person('jp',24)
# person.display()
# print()

# student = Student(name='jp',age=24,roll=42,grades=80)
# student.display()
# print()
# gs=GraduateStudent(name='jp',age=24,roll=42,grades=80,degree='MCA')
# gs.display()


########################################################

# class Academic:
#     def __init__(self, fev_subject, grade):
#         self.fev_subject = fev_subject
#         self.grade = grade

#     def display_academic_info(self):
#         print("Academic Information:")
#         print(self.fev_subject,'-',self.grade)

# class Extracurricular:
#     def __init__(self, activities, awards):
#         self.activities = activities  
#         self.awards = awards         

#     def display_extracurricular_info(self):
#         print("Extracurricular Information:")
#         print(self.activities,'-',self.awards)


# class Student(Academic, Extracurricular):
#     def __init__(self, name, age, fev_subject, grade, activities, awards):
#         Academic.__init__(self, fev_subject, grade)
#         Extracurricular.__init__(self, activities, awards)
#         self.name = name
#         self.age = age

#     def display_info(self):
#         print(f"Name: {self.name}")
#         print(f"Age: {self.age}")
#         self.display_academic_info()
#         self.display_extracurricular_info()

# student = Student('jp', 24, 'Maths', 80, 'Sports','No Awards')

# student.display_info()


#########################################


class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(self.name,self.age,end=' ')
class Student(Person):
    def __init__(self,name,age,roll,degree):
        super().__init__(name,age)
        self.roll=roll
        self.degree=degree
    def display(self):
        super().display()
        print(self.roll,self.degree,)

class GraduateStudent(Person):
    def __init__(self,name,age,degree,university):
        super().__init__(name,age)
        self.degree=degree
        self.university=university
    def display(self):
        super().display()
        print(self.degree)
        print(self.university)
