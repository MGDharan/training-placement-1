public class PalindromeChecker{
    public static boolean isPalindrome(String str){
        String cleanStr = str.replaceAll("[^a-zA-Z0-9]", "").toLowerCase();
        return new StringBuilder(cleanStr).reverse().toString().equals(cleanStr);
    }
    public static void main(String[] args){
        String str = "A man, a plan, a canal: Panama";
        if(isPalindrome(str)){
            System.out.println(str + " is a palindrome.");
        } else {
            System.out.println(str + " is not a palindrome.");
        }
    }
}