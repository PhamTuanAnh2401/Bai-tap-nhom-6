import java.util.ArrayList;
import java.util.List;

/**
 * Lớp Book đại diện cho một cuốn sách.
 */
class Book {
    private final int id;
    private final String title;
    private final String author;

    public Book(int id, String title, String author) {
        this.id = id;
        this.title = title;
        this.author = author;
    }

    public int getId() { return id; }

    public String getTitle() { return title; }

    public String getAuthor() { return author; }

    @Override
    public String toString() {
        return String.format("ID: %d | Tên sách: %s | Tác giả: %s", id, title, author);
    }
}

/**
 * Ứng dụng quản lý sách.
 */
public class BookManager {

    public static void main(String[] args) {
        List<Book> books = createBooks();

        printBooks(books);
    }

    /**
     * Tạo danh sách sách mẫu.
     */
    private static List<Book> createBooks() {
        List<Book> books = new ArrayList<>();
        books.add(new Book(1, "Lập trình C", "Nguyen Van A"));
        books.add(new Book(2, "Cấu trúc dữ liệu", "Tran Thi B"));
        return books;
    }

    /**
     * In ra danh sách sách.
     */
    private static void printBooks(List<Book> books) {
        System.out.println("Danh sách sách:");
        for (Book book : books) {
            System.out.println(book);
        }
    }
}
