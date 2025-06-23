public class  DuplicateElementRemover {
    public static int[] removeDuplicates(int[] arr) {
        if (arr == null || arr.length == 0) {
            return new int[0];
        }
        java.util.Arrays.sort(arr);
        int[] result = new int[arr.length];
        int index = 0;
        for (int i = 0; i < arr.length; i++) {
            if (i == 0 || arr[i] != arr[i - 1]) {
                result[index++] = arr[i];
            }
        }
        return java.util.Arrays.copyOf(result, index);
    }
    public static void main(String[] args) {
        int[] arr = {1, 2, 2, 3, 4, 4, 5};
        int[] uniqueArr = removeDuplicates(arr);
        System.out.print("Array with duplicates removed: ");
        for (int num : uniqueArr) {
            System.out.print(num + " ");
        }
        System.out.println();
    }
}