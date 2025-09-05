class Student:
    def __init__(self, student_id, name, major, age):
        self.student_id = student_id
        self.name = name
        self.major = major
        self.age = age

    def __str__(self):
        return f"{self.student_id} | {self.name} | {self.major} | {self.age}"


class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def show_students(self):
        for student in self.students:
            print(student)


# Demo
manager = StudentManager()
manager.add_student(Student(1, "Nam", "CNTT", 20))
manager.add_student(Student(2, "Lan", "Kinh tế", 21))
manager.show_students()
