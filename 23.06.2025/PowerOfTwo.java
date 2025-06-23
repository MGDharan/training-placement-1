public class  PowerOfTwo {
    public static boolean isPowerOfTwo(int n) {
        if (n <= 0) {
            return false;
        }
        return (n & (n - 1)) == 0;
    }
    public static void main(String[] args) {
        int n = 16;
        if (isPowerOfTwo(n)) {
            System.out.println(n + " is a power of two.");
        } else {
            System.out.println(n + " is not a power of two.");
        }
    }
}