public class  RandomNumberGenerator{
    public static int generateRandomNumber(int min, int max){
        return (int)(Math.random() * (max - min + 1)) + min;
    }
    public static void main(String[] args){
        int min = 1;
        int max = 100;
        int randomNumber = generateRandomNumber(min, max);
        System.out.println("Random number between " + min + " and " + max + ": " + randomNumber);
    }
}