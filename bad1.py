class Student:
    """Class đại diện cho một sinh viên."""

    def __init__(self, student_id, name, major, age):
        self.student_id = student_id
        self.name = name
        self.major = major
        self.age = age

    def __str__(self):
        return f"{self.student_id} | {self.name} | {self.major} | {self.age}"


class StudentManager:
    """Class quản lý danh sách sinh viên."""

    def __init__(self):
        self.students = []

    def add_student(self, student):
        if isinstance(student, Student):
            self.students.append(student)
        else:
            raise TypeError("Only Student instances can be added.")

    def show_students(self):
        print("Danh sách sinh viên:")
        for student in self.students:
            print(student)


# Demo
if __name__ == "__main__":
    student_manager = StudentManager()
    student_manager.add_student(Student(1, "Nam", "CNTT", 20))
    student_manager.add_student(Student(2, "Lan", "Kinh tế", 21))

    student_manager.show_students()
