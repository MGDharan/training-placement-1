public class TwoDimensionalArray {

    public static void main(String[] args) {
        int[][] matrix = {
                {1, 2, 3},
                {4, 5, 6},
                {7, 8, 9}
        };

        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[i].length; j++) {
                System.out.print(matrix[i][j] + " ");
            }
            System.out.println();
        }

        int sum = 0;
        for(int[] row : matrix){
            for(int num : row){
                sum += num;
            }
        }
        System.out.println("Sum of all elements: " + sum);
    }
}