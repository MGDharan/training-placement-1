public class  IsomorphicStrings {
    public static boolean areIsomorphic(String s1, String s2) {
        if (s1.length() != s2.length()) {
            return false;
        }
        java.util.Map<Character, Character> map = new java.util.HashMap<>();
        java.util.Set<Character> usedChars = new java.util.HashSet<>();
        for (int i = 0; i < s1.length(); i++) {
            char c1 = s1.charAt(i);
            char c2 = s2.charAt(i);
            if (map.containsKey(c1)) {
                if (map.get(c1) != c2) {
                    return false;
                }
            } else {
                if (usedChars.contains(c2)) {
                    return false;
                }
                map.put(c1, c2);
                usedChars.add(c2);
            }
        }
        return true;
    }
    public static void main(String[] args) {
        String s1 = "egg";
        String s2 = "add";
        if (areIsomorphic(s1, s2)) {
            System.out.println(s1 + " and " + s2 + " are isomorphic.");
        } else {
            System.out.println(s1 + " and " + s2 + " are not isomorphic.");
        }
    }
}