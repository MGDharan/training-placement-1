public class ArrayMaxFinder {
    public static int findMax(int[] arr) {
        int max = arr[0];
        for (int i = 1; i < arr.length; i++) {
            if (arr[i] > max) {
                max = arr[i];
            }
        }
        return max;
    }
    public static void main(String[] args) {
        int[] arr = {10, 5, 20, 15, 25};
        System.out.println("Maximum value in array: " + findMax(arr));
    }
}