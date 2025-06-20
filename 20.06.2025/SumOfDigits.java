public class SumOfDigits {
    public static int sumDigits(int n) {
        if (n < 0) {
            n = -n;
        }
        int sum = 0;
        while (n > 0) {
            sum += n % 10;
            n /= 10;
        }
        return sum;
    }

    public static void main(String[] args) {
        int number = 12345;
        int sum = sumDigits(number);
        System.out.println("Sum of digits of " + number + ": " + sum);
    }
}