class Book:
    def __init__(self, book_id, title, author, year, status="available"):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.status = status
    
    def __str__(self):
        return f"{self.book_id}|{self.title}|{self.author}|{self.year}|{self.status}"
    
    @classmethod
    def from_string(cls, book_string):
        """Tạo đối tượng Book từ chuỗi dạng 'id|title|author|year|status'"""
        parts = book_string.split("|")
        return cls(parts[0], parts[1], parts[2], parts[3], parts[4])
    
    def borrow(self):
        """Mượn sách"""
        if self.status == "available":
            self.status = "borrowed"
            return True
        return False
    
    def return_book(self):
        """Trả sách"""
        if self.status == "borrowed":
            self.status = "available"
            return True
        return False

books = []

<<<<<<< HEAD
from typing import List, Dict

def add_book(books_list: List[Dict], book: Dict) -> None:
    """
    Thêm một sách vào danh sách sách.

    Args:
        books_list (List[Dict]): Danh sách sách hiện có.
        book (Dict): Thông tin sách cần thêm, ví dụ {'title': str, 'author': str}.
    """
    books_list.append(book)
# def add_book(book):
#     """Thêm sách vào danh sách"""
#     books.append(book)

def show_books():
    """Hiển thị tất cả sách dưới dạng bảng"""
    if not books:
        print("Danh sách sách trống!")
        return

    # In tiêu đề bảng
    print(f"{'ID':<5} {'Title':<25} {'Author':<20} {'Year':<6} {'Status':<10}")
    print("-" * 70)

    # In từng sách
    for b in books:
        print(f"{b.book_id:<5} {b.title:<25} {b.author:<20} {b.year:<6} {b.status:<10}")

def show_books():
    """Hiển thị tất cả sách"""
    for b in books:
        print(b)

def find_book_by_id(book_id):
    """Tìm sách theo ID"""
    for b in books:
        if b.book_id == book_id:
            print("Found:", b)
            return b
    print(f"Book with ID {book_id} not found")
    return None

def delete_book(book_id):
    """Xóa sách theo ID"""
    for i, b in enumerate(books):
        if b.book_id == book_id:
            removed_book = books.pop(i)
            print(f"Deleted: {removed_book}")
            return True
    print(f"Book with ID {book_id} not found")
    return False

def update_book(book_id, title=None, author=None, year=None, status=None):
    """Cập nhật thông tin sách"""
    book = find_book_by_id(book_id)
    if book:
        if title:
            book.title = title
        if author:
            book.author = author
        if year:
            book.year = year
        if status:
            book.status = status
        print(f"Updated: {book}")
        return True
    return False

def borrow_book(book_id):
    """Mượn sách"""
    book = find_book_by_id(book_id)
    if book:
        if book.borrow():
            print(f"Book '{book.title}' has been borrowed")
            return True
        else:
            print(f"Book '{book.title}' is not available for borrowing")
            return False
    return False

def return_book(book_id):
    """Trả sách"""
    book = find_book_by_id(book_id)
    if book:
        if book.return_book():
            print(f"Book '{book.title}' has been returned")
            return True
        else:
            print(f"Book '{book.title}' was not borrowed")
            return False
    return False

def count_books():
    """Đếm tổng số sách"""
    print("Total books:", len(books))
    return len(books)

# Demo dữ liệu ban đầu
add_book(Book("1", "Lập trình Python", "Nguyen Van A", "2020", "available"))
add_book(Book("2", "Trí tuệ nhân tạo", "Tran Thi B", "2021", "available"))
add_book(Book("3", "Cơ sở dữ liệu", "Le Van C", "2019", "borrowed"))

print("All books:")
show_books()

print("\nFinding book with ID '2':")
find_book_by_id("2")

print("\nBorrowing book with ID '1':")
borrow_book("1")

print("\nReturning book with ID '3':")
return_book("3")

print("\nUpdating book with ID '2':")
update_book("2", title="AI nâng cao", author="Tran Thi B", year="2022", status="available")

print("\nDeleting book with ID '3':")
delete_book("3")

print("\nCounting books:")
count_books()

print("\nAll books after changes:")
show_books()

# Demo thêm sách từ chuỗi
print("\nAdding book from string:")
new_book = Book.from_string("4|Toán cao cấp|Pham Van D|2020|available")
add_book(new_book)
show_books()

# Demo thử mượn sách không có sẵn
print("\nTrying to borrow unavailable book:")
borrow_book("1")  # Đã mượn từ trước
#commett test