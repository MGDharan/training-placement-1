public class SimpleCalculator{
    public static double calculate(double num1, double num2, char operator){
        switch(operator){
            case '+': return num1 + num2;
            case '-': return num1 - num2;
            case '*': return num1 * num2;
            case '/': 
                if(num2 == 0){
                    throw new ArithmeticException("Cannot divide by zero.");
                }
                return num1 / num2;
            default: throw new IllegalArgumentException("Invalid operator.");
        }
    }
    public static void main(String[] args){
        double result = calculate(10, 5, '+');
        System.out.println("Result: " + result);
    }
}