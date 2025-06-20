public class TemperatureConverter {
    public static double celsiusToFahrenheit(double celsius) {
        return (celsius * 9 / 5) + 32;
    }

    public static double fahrenheitToCelsius(double fahrenheit) {
        return (fahrenheit - 32) * 5 / 9;
    }

    public static void main(String[] args) {
        System.out.println("0 Celsius is " + celsiusToFahrenheit(0) + " Fahrenheit.");
        System.out.println("32 Fahrenheit is " + fahrenheitToCelsius(32) + " Celsius.");
    }
}