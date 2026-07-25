class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)
        x = len(s1)
        for i in range(len(s2)- x +1):
            w = s2[i:i+x]
            w = sorted(w)
            if w==s1:
                return True
            else:
                continue
        return False