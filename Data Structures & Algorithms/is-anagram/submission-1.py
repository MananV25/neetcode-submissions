class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        m = sorted(s)
        n = sorted(t)
        if m == n:
            return True
        return False