public class ArraySorter{
    public static void sortArray(int[] arr){
        java.util.Arrays.sort(arr);
    }
    public static void main(String[] args){
        int[] arr = {5,2,8,1,9,4};
        sortArray(arr);
        System.out.print("Sorted array: ");
        for(int num : arr){
            System.out.print(num + " ");
        }
        System.out.println();
    }
}