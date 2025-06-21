public class FibonacciSeries {
    public static void generateFibonacci(int n) {
        int a = 0, b = 1;
        System.out.print(a + " " + b);
        for (int i = 2; i < n; i++) {
            int c = a + b;
            System.out.print(" " + c);
            a = b;
            b = c;
        }
    }
    public static void main(String[] args) {
        java.util.Scanner scanner = new java.util.Scanner(System.in);
        System.out.print("Enter number of terms: ");
        int n = scanner.nextInt();
        generateFibonacci(n);
        scanner.close();
    }
}