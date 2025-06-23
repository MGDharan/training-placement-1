public class  ReverseWordsInString {
    public static String reverseWords(String s) {
        String[] words = s.trim().split("\\s+");
        StringBuilder sb = new StringBuilder();
        for (int i = words.length - 1; i >= 0; i--) {
            sb.append(words[i]).append(" ");
        }
        return sb.toString().trim();
    }
    public static void main(String[] args) {
        String s = "the sky is blue";
        String reversed = reverseWords(s);
        System.out.println("Reversed string: " + reversed);
    }
}