# USING CONSTRUCTOR

class Student:
    school_name = "ABC International School"

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade


s1 = Student("Unik", "10th")

print(s1.name)  # Unik
print(s1.grade) # 10th

print(s1.school_name)  # ABC International School
print(Student.school_name)  # ABC International School


'''
OP:

Unik
10th
ABC International School
ABC International School
'''
