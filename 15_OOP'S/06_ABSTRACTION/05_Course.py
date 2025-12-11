from abc import ABC, abstractmethod

class Course(ABC):

    def validate_student(self,student_name):
        if len(student_name) == 0:
            print('Invalid Student Name..!')
            return False
        return True

    @abstractmethod
    def calculate_duration(self):
        pass

    @abstractmethod
    def start_course(self,student_name):
        pass

class PythonCourse(Course):

    def __init__(self):
        self.modules = 12
        self.hours_per_module = 2

    def calculate_duration(self):
        return self.modules * self.hours_per_module

    def start_course(self,student_name):
        if self.validate_student(student_name):
            total_hours = self.calculate_duration()
            print(f'Python Course Started for {student_name}. Total Duration: {total_hours} Hours')

py_obj = PythonCourse()
py_obj.start_course('UNiK')

'''
OUTPUT : 

Python Course Started for UNiK. Total Duration: 24 Hours
'''
