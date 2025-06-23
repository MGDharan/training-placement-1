public class FactorialCalculator{
    public static long factorial(int n){
        if(n < 0){
            throw new IllegalArgumentException("Input must be non-negative.");
        }
        if(n == 0){
            return 1;
        }
        long fact = 1;
        for(int i = 1; i <= n; i++){
            fact *= i;
        }
        return fact;
    }
    public static void main(String[] args){
        int num = 5;
        long fact = factorial(num);
        System.out.println("Factorial of " + num + " is: " + fact);
    }
}