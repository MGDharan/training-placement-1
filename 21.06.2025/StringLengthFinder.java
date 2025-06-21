public class StringLengthFinder {
    public static int stringLength(String str) {
        return str.length();
    }
    public static void main(String[] args) {
        java.util.Scanner scanner = new java.util.Scanner(System.in);
        System.out.print("Enter a string: ");
        String str = scanner.nextLine();
        System.out.println("Length of string: " + stringLength(str));
        scanner.close();
    }
}