def is_palindrome(s):
    return s == s[::-1]

def partition_palindromes(s):
    result = []

    def backtrack(start, path):
        if start == len(s):
            result.append(path[:])
            return
        for end in range(start + 1, len(s) + 1):
            part = s[start:end]
            if is_palindrome(part):
                path.append(part)
                backtrack(end, path)
                path.pop()

    backtrack(0, [])
    return result

# Example usage:
s = "aab"
print(partition_palindromes(s))
# Output: [['a', 'a', 'b'], ['aa', 'b']]
