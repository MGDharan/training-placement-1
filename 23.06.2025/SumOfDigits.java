public class  SumOfDigits {
    public static int sumDigits(int number) {
        if (number < 0) {
            number = -number;
        }
        int sum = 0;
        while (number > 0) {
            sum += number % 10;
            number /= 10;
        }
        return sum;
    }
    public static void main(String[] args) {
        int num = 12345;
        int sum = sumDigits(num);
        System.out.println("Sum of digits of " + num + ": " + sum);
    }
}