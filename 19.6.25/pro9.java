public class Armstrong {
    public static void main(String[] args) {
        int num = 153, temp = num, sum = 0;
        while (num > 0) {
            int digit = num % 10;
            sum += digit * digit * digit;
            num /= 10;
        }
        System.out.println(temp == sum ? "Armstrong" : "Not Armstrong");
    }
}
