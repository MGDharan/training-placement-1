public class PowerCalculator {
    public static double power(double base, int exponent) {
        return Math.pow(base, exponent);
    }

    public static void main(String[] args) {
        System.out.println("2 to the power of 3 is: " + power(2, 3));
        System.out.println("5 to the power of 2 is: " + power(5, 2));

    }
}