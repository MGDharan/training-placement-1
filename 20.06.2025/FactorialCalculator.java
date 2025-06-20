public class FactorialCalculator {
    public static long factorial(int n) {
        if (n < 0) {
            throw new IllegalArgumentException("Input must be non-negative.");
        }
        if (n == 0) {
            return 1;
        }
        long result = 1;
        for (int i = 1; i <= n; i++) {
            result *= i;
        }
        return result;
    }

    public static void main(String[] args) {
        java.util.Scanner scanner = new java.util.Scanner(System.in);
        System.out.print("Enter a non-negative integer: ");
        int num = scanner.nextInt();
        try {
            long fact = factorial(num);
            System.out.println("Factorial of " + num + " is: " + fact);
        } catch (IllegalArgumentException e) {
            System.out.println(e.getMessage());
        }
        scanner.close();
    }
}