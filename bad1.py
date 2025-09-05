students = []

def add_student(s):
    students.append(s)

def show_students():
    for s in students:
        print(s)

add_student("1|Nam|CNTT|20")
add_student("2|Lan|KinhTe|21")
show_students()