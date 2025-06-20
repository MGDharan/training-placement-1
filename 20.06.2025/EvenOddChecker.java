public class EvenOddChecker {
    public static boolean isEven(int num) {
        return num % 2 == 0;
    }

    public static void main(String[] args) {
        System.out.println("Is 10 even? " + isEven(10));
        System.out.println("Is 7 even? " + isEven(7));
    }
}