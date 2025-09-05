# BAD CODE: Quản lý sách thư viện kiểu thủ công, không class, không cấu trúc
# Dữ liệu lưu dưới dạng "id|title|author|year|status"

books = []

def add_book(b):
    books.append(b)

def show_books():
    for b in books:
        print(b)

def find_book_by_id(book_id):
    for b in books:
        if b.split("|")[0] == book_id:
            print("Found:", b)

def delete_book(book_id):
    for b in books:
        if b.split("|")[0] == book_id:
            books.remove(b)

def update_book(book_id, new_value):
    for i in range(len(books)):
        if books[i].split("|")[0] == book_id:
            books[i] = new_value

def borrow_book(book_id):
    for i in range(len(books)):
        if books[i].split("|")[0] == book_id:
            parts = books[i].split("|")
            if parts[4] == "available":
                parts[4] = "borrowed"
                books[i] = "|".join(parts)

def return_book(book_id):
    for i in range(len(books)):
        if books[i].split("|")[0] == book_id:
            parts = books[i].split("|")
            if parts[4] == "borrowed":
                parts[4] = "available"
                books[i] = "|".join(parts)

def count_books():
    print("Total books:", len(books))

# Demo dữ liệu ban đầu
add_book("1|Lập trình Python|Nguyen Van A|2020|available")
add_book("2|Trí tuệ nhân tạo|Tran Thi B|2021|available")
add_book("3|Cơ sở dữ liệu|Le Van C|2019|borrowed")

show_books()
find_book_by_id("2")
borrow_book("1")
return_book("3")
update_book("2", "2|AI nâng cao|Tran Thi B|2022|available")
delete_book("3")
count_books()
show_books()
