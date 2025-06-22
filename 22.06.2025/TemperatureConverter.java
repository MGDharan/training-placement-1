public class TemperatureConverter {

    public static double celsiusToFahrenheit(double celsius) {
        return (celsius * 9/5) + 32;
    }

    public static double fahrenheitToCelsius(double fahrenheit) {
        return (fahrenheit - 32) * 5/9;
    }

    public static void main(String[] args) {
        double celsius = 25;
        double fahrenheit = 77;

        System.out.println(celsius + " degrees Celsius is equal to " + celsiusToFahrenheit(celsius) + " degrees Fahrenheit.");
        System.out.println(fahrenheit + " degrees Fahrenheit is equal to " + fahrenheitToCelsius(fahrenheit) + " degrees Celsius.");
    }
}