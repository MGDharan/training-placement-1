public class  CountOccurrencesOfCharacter {
    public static int countOccurrences(String str, char ch) {
        int count = 0;
        for (char c : str.toCharArray()) {
            if (c == ch) {
                count++;
            }
        }
        return count;
    }
    public static void main(String[] args) {
        String str = "hello world";
        char ch = 'l';
        int count = countOccurrences(str, ch);
        System.out.println("Occurrences of '" + ch + "': " + count);
    }
}