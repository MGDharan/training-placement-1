public class EvenOddChecker {
    public static String checkEvenOdd(int num) {
        return (num % 2 == 0) ? "Even" : "Odd";
    }

    public static void main(String[] args) {
        java.util.Scanner scanner = new java.util.Scanner(System.in);
        System.out.print("Enter an integer: ");
        int num = scanner.nextInt();
        System.out.println(checkEvenOdd(num));
        scanner.close();
    }
}