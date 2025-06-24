public class  CombinationSumII {
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        List<List<Integer>> result = new ArrayList<>();
        Arrays.sort(candidates);
        backtrack(result, new ArrayList<>(), candidates, target, 0);
        return result;
    }
    private void backtrack(List<List<Integer>> result, List<Integer> combination, int[] candidates, int target, int start) {
        if (target == 0) {
            result.add(new ArrayList<>(combination));
            return;
        }
        if (target < 0) return;
        for (int i = start; i < candidates.length; i++) {
            if (i > start && candidates[i] == candidates[i - 1]) continue;
            combination.add(candidates[i]);
            backtrack(result, combination, candidates, target - candidates[i], i + 1);
            combination.remove(combination.size() - 1);
        }
    }
}