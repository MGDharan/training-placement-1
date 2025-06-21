public class CharacterFrequencyCounter {
    public static void countCharacterFrequency(String text) {
        if (text == null || text.isEmpty()) {
            return;
        }
        java.util.Map<Character, Integer> charFrequency = new java.util.HashMap<>();
        for (char c : text.toCharArray()) {
            charFrequency.put(c, charFrequency.getOrDefault(c, 0) + 1);
        }
        for (java.util.Map.Entry<Character, Integer> entry : charFrequency.entrySet()) {
            System.out.println(entry.getKey() + ": " + entry.getValue());
        }
    }

    public static void main(String[] args) {
        String text = "Programming is fun!";
        countCharacterFrequency(text);
    }
}