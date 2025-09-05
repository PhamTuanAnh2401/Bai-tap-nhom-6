import java.util.ArrayList;
import java.util.List;

// Lớp Book thể hiện 1 cuốn sách
class Book {
    private int id;
    private String title;
    private String author;

    // Constructor
    public Book(int id, String title, String author) {
        this.id = id;
        this.title = title;
        this.author = author;
    }

    // Getter
    public int getId() { return id; }
    public String getTitle() { return title; }
    public String getAuthor() { return author; }

    // toString để in sách rõ ràng
    @Override
    public String toString() {
        return String.format("ID: %d | Tên sách: %s | Tác giả: %s", id, title, author);
    }
}

public class CleanCode {
    public static void main(String[] args) {
        // Dùng List thay vì ArrayList để dễ thay đổi
        List<Book> books = new ArrayList<>();

        books.add(new Book(1, "Lập trình C", "Nguyen Van A"));
        books.add(new Book(2, "Cấu trúc dữ liệu", "Tran Thi B"));

        for (Book book : books) {
            System.out.println(book);
        }
    }
}
