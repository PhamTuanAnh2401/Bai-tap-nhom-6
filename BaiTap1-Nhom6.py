students = []

def add_student(s):
    students.append(s)

def show_students():
    for s in students:
        print(s)

def find_student_by_id(student_id):
    for s in students:
        if s.split("|")[0] == student_id:
            print("Found:", s)

def delete_student(student_id):
    for s in students:
        if s.split("|")[0] == student_id:
            students.remove(s)

def update_student(student_id, new_value):
    for i in range(len(students)):
        if students[i].split("|")[0] == student_id:
            students[i] = new_value

# Demo thêm dữ liệu
add_student("1|Nam|CNTT|20")
add_student("2|Lan|KinhTe|21")
add_student("3|Hung|Y|22")
add_student("4|Mai|CNTT|23")

show_students()
find_student_by_id("2")
delete_student("3")
update_student("4", "4|Mai|KinhTe|25")
show_students()