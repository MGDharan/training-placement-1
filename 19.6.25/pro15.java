public class CountDigits {
    public static void main(String[] args) {
        int num = 12345, count = 0;
        while (num != 0) {
            count++;
            num /= 10;
        }
        System.out.println("Digits: " + count);
    }
}
