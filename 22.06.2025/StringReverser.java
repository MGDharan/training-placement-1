public class StringReverser {

    public static String reverseString(String str) {
        if (str == null || str.isEmpty()) {
            return str;
        }
        return new StringBuilder(str).reverse().toString();
    }

    public static void main(String[] args) {
        String inputString = "hello world";
        String reversedString = reverseString(inputString);
        System.out.println("Reversed string: " + reversedString);
    }
}