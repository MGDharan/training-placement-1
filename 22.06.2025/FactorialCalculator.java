public class FactorialCalculator {
    public static long factorial(int n) {
        if (n < 0) throw new IllegalArgumentException("Input must be non-negative");
        if (n == 0) return 1;
        long result = 1;
        for (int i = 1; i <= n; i++) {
            result *= i;
        }
        return result;
    }
    public static void main(String[] args) {
        int num = 5;
        System.out.println("Factorial of " + num + ": " + factorial(num));
    }
}