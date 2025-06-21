public class MultiplicationTable {
    public static void generateTable(int num) {
        for (int i = 1; i <= 10; i++) {
            System.out.println(num + " x " + i + " = " + (num * i));
        }
    }
    public static void main(String[] args) {
        java.util.Scanner scanner = new java.util.Scanner(System.in);
        System.out.print("Enter a number: ");
        int num = scanner.nextInt();
        generateTable(num);
        scanner.close();
    }
}