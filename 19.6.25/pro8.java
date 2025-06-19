public class Palindrome {
    public static void main(String[] args) {
        int num = 121, rev = 0, temp = num;
        while (num != 0) {
            rev = rev * 10 + num % 10;
            num /= 10;
        }
        System.out.println(temp == rev ? "Palindrome" : "Not Palindrome");
    }
}
