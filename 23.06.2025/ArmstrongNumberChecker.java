public class  ArmstrongNumberChecker {
    public static boolean isArmstrong(int num) {
        int originalNum = num;
        int numDigits = String.valueOf(num).length();
        int sum = 0;
        while (num > 0) {
            int digit = num % 10;
            sum += Math.pow(digit, numDigits);
            num /= 10;
        }
        return sum == originalNum;
    }
    public static void main(String[] args) {
        int num = 153;
        if (isArmstrong(num)) {
            System.out.println(num + " is an Armstrong number.");
        } else {
            System.out.println(num + " is not an Armstrong number.");
        }
    }
}