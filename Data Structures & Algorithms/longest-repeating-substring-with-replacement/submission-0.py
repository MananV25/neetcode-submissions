class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxLength = 0
        left = 0
        count = {}
        maxFreq = 0
        
        for right in range(len(s)):
            # Add current character to the window
            count[s[right]] = count.get(s[right], 0) + 1

            # Update the highest frequency character in the window
            maxFreq = max(maxFreq, count[s[right]])

            # If more than k replacements are needed,
            # shrink the window from the left
            while (right - left + 1) - maxFreq > k:
                count[s[left]] -= 1
                left += 1

            # Update the answer
            maxLength = max(maxLength, right - left + 1)

        return maxLength

        
                


