class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        sub = []
        def ispalindrome(word):
            return word == word[::-1]
        def backtrack(start):
            if start == len(s):
                res.append(sub.copy())
                return
            for i in range(start, len(s)):
                word = s[start:i+1]
                if ispalindrome(word):
                    sub.append(word)
                    backtrack(i+1)
                    sub.pop()
        backtrack(0)
        return res
