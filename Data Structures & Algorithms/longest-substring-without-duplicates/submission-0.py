class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        ml = 0
        left = 0
        for i in range(len(s)):
            if s[i] not in seen:
                seen.add(s[i])
                ml = max(ml,i - left + 1)
            else :
                while s[i] in seen:
                    
                    seen.remove(s[left])
                    
                    left+=1
                    ml = max(ml,i - left + 1)
                seen.add(s[i])
        return ml

