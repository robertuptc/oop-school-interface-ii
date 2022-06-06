from classes.staff import Staff
from classes.student import Student
import csv
import os.path

class School:
    def __init__(self, name):
        self.name = name
        self.staff = Staff.objects()
        self.students = Student.objects()

    @classmethod
    def list_students(cls):
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../data/students.csv")
        with open(path) as csvfile:
            reader = csv.DictReader(csvfile)
            for idx, row in enumerate(reader):
                print(f"{idx+1}. {row['name']} {row['school_id']}")

    @classmethod
    def find_student_by_id(cls, student_id):
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../data/students.csv")
        with open(path) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['school_id'] == student_id:
                    return (Student(**dict(row)))


# School.find_student_by_id()

