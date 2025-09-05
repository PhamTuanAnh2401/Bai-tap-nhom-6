from typing import List, Optional

class Student:
    def __init__(self, student_id: int, name: str, major: str, age: int) -> None:
        self.student_id = student_id
        self.name = name
        self.major = major
        self.age = age

    def __str__(self) -> str:
        return f"{self.student_id} | {self.name} | {self.major} | {self.age}"


class StudentManager:
    def __init__(self) -> None:
        self.students: List[Student] = []

    def add_student(self, student: Student) -> None:
        self.students.append(student)

    def get_all_students(self) -> List[Student]:
        return self.students

    def find_student(self, student_id: int) -> Optional[Student]:
        return next((s for s in self.students if s.student_id == student_id), None)

    def remove_student(self, student_id: int) -> bool:
        student = self.find_student(student_id)
        if student:
            self.students.remove(student)
            return True
        return False

    def update_student(self, student_id: int, name: str = None, major: str = None, age: int = None) -> bool:
        student = self.find_student(student_id)
        if not student:
            return False
        if name: student.name = name
        if major: student.major = major
        if age: student.age = age
        return True


# Demo
if __name__ == "__main__":
    manager = StudentManager()
    manager.add_student(Student(1, "Nam", "CNTT", 20))
    manager.add_student(Student(2, "Lan", "Kinh tế", 21))

    print("📌 Danh sách sinh viên:")
    for s in manager.get_all_students():
        print(s)

    print("\nTìm sinh viên ID=2:")
    print(manager.find_student(2))

    print("\nXóa sinh viên ID=1:")
    manager.remove_student(1)

    print("\nDanh sách sau khi xóa:")
    for s in manager.get_all_students():
        print(s)

    print("\nCập nhật thông tin sinh viên ID=2:")
    manager.update_student(2, name="Lan Nguyễn", age=22)
    for s in manager.get_all_students():
        print(s)
# comment vi du moi
