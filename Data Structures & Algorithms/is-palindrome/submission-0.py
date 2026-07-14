class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = s.strip().lower()
        s = "".join(char for char in s if char.isalnum())
        s = s.replace(" ","")
        m = s[::-1]
        if s==m:
            return True
        else:
            return False
