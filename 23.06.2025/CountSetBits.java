public class  CountSetBits {
    public static int countSetBits(int n) {
        int count = 0;
        while (n > 0) {
            count += (n & 1);
            n >>= 1;
        }
        return count;
    }
    public static void main(String[] args) {
        int n = 15;
        int count = countSetBits(n);
        System.out.println("Number of set bits in " + n + ": " + count);
    }
}