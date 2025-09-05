import java.util.*;

public class BadCode {
    public static void main(String[] args) {
        ArrayList<String> books = new ArrayList<>();
        books.add("1|Lập trình C|Nguyen Van A");
        books.add("2|Cấu trúc dữ liệu|Tran Thi B");

        for (String b : books) {
            System.out.println(b);
        }
    }
}