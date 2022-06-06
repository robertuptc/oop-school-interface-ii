import csv
import os.path
from classes.person import Person

class Student(Person):

    def __init__(self, name, age, password, role, school_id):
        super().__init__(name, age, password, role)
        self.school_id = school_id

    @classmethod
    def objects(cls):
        students = []
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../data/students.csv")
        with open(path) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                students.append(Student(**dict(row)))
                # print(row)
        return students
        # print(list(students))

    def __str__(self):
        return f"""{self.name.upper()}
---------------
age : {self.age}
id : {self.school_id}
        """
        # return f"{self.name.upper()}\n--------------- \nage : {self.age}\nid : {self.school_id}"  //another way to get the same result as the one above

# Student.objects()
# print(Student("Lisa", 25, "Student", "13345" , "xx"))
