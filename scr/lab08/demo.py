from models import Student
from serialize import students_from_json, students_to_json

'''student = Student("Петров Петр Петрович", "2007-05-05", "BIVT-05", 4.2)
print(student)
student = Student("Петров Петр Петрович", "207-05-05", "BIVT-05", 4.2)
print(student)'''

for s in students_from_json("data/lab08/samples/student.json"):
    print(s)

students = [
    Student(fio="Иванов Иван Иванович", birthdate="2005-01-17", group="BIVT-05", gpa=3.0),
    Student(fio="Петров Петр Петрович", birthdate="2007-05-15", group="BIVT-05", gpa=3.5),
    Student(fio="Константинов Константин Константинович", birthdate="2006-06-06", group="BIVT-06", gpa=2.8),
]

students_to_json(students, "data/lab08/out/students_out.json")