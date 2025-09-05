class Student:
    def __init__(self, student_id, name, major, age):
        self.student_id = student_id
        self.name = name
        self.major = major
        self.age = age
    
    def __str__(self):
        return f"{self.student_id}|{self.name}|{self.major}|{self.age}"
    
    @classmethod
    def from_string(cls, student_string):
        """Tạo đối tượng Student từ chuỗi dạng 'id|name|major|age'"""
        parts = student_string.split("|")
        return cls(parts[0], parts[1], parts[2], int(parts[3]))

students = []

def add_student(students_list, student):
    """
    Thêm một sinh viên vào danh sách sinh viên.
    
    Args:
        students_list (list): Danh sách sinh viên hiện có.
        student (dict): Thông tin sinh viên cần thêm.
    """
    students_list.append(student)
    return students_list


# def show_students():
#     """Hiển thị tất cả sinh viên"""
#     for s in students:
#         print(s)

def show_students():
    """Hiển thị tất cả sinh viên dưới dạng bảng"""
    if not students:
        print("Danh sách sinh viên trống!")
        return

    # In tiêu đề bảng
    print(f"{'ID':<5} {'Name':<15} {'Major':<10} {'Age':<5}")
    print("-" * 40)

    # In từng sinh viên
    for s in students:
        print(f"{s.student_id:<5} {s.name:<15} {s.major:<10} {s.age:<5}")


def find_student_by_id(student_id):
    """Tìm sinh viên theo ID"""
    for s in students:
        if s.student_id == student_id:
            print("Found:", s)
            return s
    print(f"Student with ID {student_id} not found")
    return None

def delete_student(student_id):
    """Xóa sinh viên theo ID"""
    for i, s in enumerate(students):
        if s.student_id == student_id:
            removed_student = students.pop(i)
            print(f"Deleted: {removed_student}")
            return True
    print(f"Student with ID {student_id} not found")
    return False

def update_student(student_id, name=None, major=None, age=None):
    """Cập nhật thông tin sinh viên"""
    student = find_student_by_id(student_id)
    if student:
        if name:
            student.name = name
        if major:
            student.major = major
        if age:
            student.age = age
        print(f"Updated: {student}")
        return True
    return False

# Demo thêm dữ liệu
add_student(Student("1", "Nam", "CNTT", 20))
add_student(Student("2", "Lan", "KinhTe", 21))
add_student(Student("3", "Hung", "Y", 22))
add_student(Student("4", "Mai", "CNTT", 23))

print("All students:")
show_students()

print("\nFinding student with ID '2':")
find_student_by_id("2")

print("\nDeleting student with ID '3':")
delete_student("3")

print("\nUpdating student with ID '4':")
update_student("4", name="Mai", major="KinhTe", age=25)

print("\nAll students after changes:")
show_students()

# Demo chuyển đổi từ chuỗi sang đối tượng Student
print("\nAdding student from string:")
new_student = Student.from_string("5|Hoa|Duoc|24")
add_student(new_student)
show_students()