public class LargestNumberFinder {
    public static int findLargest(int[] numbers) {
        if (numbers == null || numbers.length == 0) {
            throw new IllegalArgumentException("Array cannot be null or empty.");
        }
        int largest = numbers[0];
        for (int i = 1; i < numbers.length; i++) {
            if (numbers[i] > largest) {
                largest = numbers[i];
            }
        }
        return largest;
    }

    public static void main(String[] args) {
        int[] numbers = {10, 5, 20, 15, 25};
        int largest = findLargest(numbers);
        System.out.println("Largest number: " + largest);
    }
}