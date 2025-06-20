public class StringManipulator {
    public static String reverseString(String str) {
        return new StringBuilder(str).reverse().toString();
    }

    public static void main(String[] args) {
        String str = "hello";
        String reversedStr = reverseString(str);
        System.out.println("Reversed string: " + reversedStr);
    }
}