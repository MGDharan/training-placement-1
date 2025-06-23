public class VowelCounter{
    public static int countVowels(String str){
        int count = 0;
        String vowels = "aeiouAEIOU";
        for(char c : str.toCharArray()){
            if(vowels.indexOf(c) != -1){
                count++;
            }
        }
        return count;
    }
    public static void main(String[] args){
        String str = "Hello World";
        int vowelCount = countVowels(str);
        System.out.println("Number of vowels: " + vowelCount);
    }
}