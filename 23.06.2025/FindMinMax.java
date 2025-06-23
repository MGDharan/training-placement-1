public class  FindMinMax {
    public static int[] findMinMax(int[] arr) {
        if (arr == null || arr.length == 0) {
            return new int[0];
        }
        int min = arr[0];
        int max = arr[0];
        for (int i = 1; i < arr.length; i++) {
            if (arr[i] < min) {
                min = arr[i];
            }
            if (arr[i] > max) {
                max = arr[i];
            }
        }
        return new int[] { min, max };
    }
    public static void main(String[] args) {
        int[] arr = {3, 1, 4, 1, 5, 9, 2, 6};
        int[] minMax = findMinMax(arr);
        System.out.println("Min: " + minMax[0] + ", Max: " + minMax[1]);
    }
}