def permute_unique(nums):
    res = []
    nums.sort()
    used = [False] * len(nums)

    def backtrack(path):
        if len(path) == len(nums):
            res.append(path[:])
            return
        for i in range(len(nums)):
            if used[i] or (i > 0 and nums[i] == nums[i - 1] and not used[i - 1]):
                continue
            used[i] = True
            backtrack(path + [nums[i]])
            used[i] = False

    backtrack([])
    return res

print(permute_unique([1, 1, 2]))
