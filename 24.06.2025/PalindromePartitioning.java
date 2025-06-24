public class  PalindromePartitioning {
    public List<List<String>> partition(String s) {
        List<List<String>> result = new ArrayList<>();
        backtrack(result, new ArrayList<>(), s, 0);
        return result;
    }
    private void backtrack(List<List<String>> result, List<String> partition, String s, int start) {
        if (start == s.length()) {
            result.add(new ArrayList<>(partition));
            return;
        }
        for (int i = start; i < s.length(); i++) {
            if (isPalindrome(s, start, i)) {
                partition.add(s.substring(start, i + 1));
                backtrack(result, partition, s, i + 1);
                partition.remove(partition.size() - 1);
            }
        }
    }
    private boolean isPalindrome(String s, int start, int end) {
        while (start < end) {
            if (s.charAt(start) != s.charAt(end)) return false;
            start++;
            end--;
        }
        return true;
    }
}