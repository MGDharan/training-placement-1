public class PrimeNumberGenerator {
    public static void generatePrimes(int limit) {
        for (int i = 2; i <= limit; i++) {
            boolean isPrime = true;
            for (int j = 2; j <= Math.sqrt(i); j++) {
                if (i % j == 0) {
                    isPrime = false;
                    break;
                }
            }
            if (isPrime) {
                System.out.print(i + " ");
            }
        }
    }
    public static void main(String[] args) {
        java.util.Scanner scanner = new java.util.Scanner(System.in);
        System.out.print("Enter the limit: ");
        int limit = scanner.nextInt();
        generatePrimes(limit);
        scanner.close();
    }
}