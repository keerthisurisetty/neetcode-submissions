class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = str(s)
        sLower = s.lower()
        sClean = ''.join(c for c in sLower if c.isalnum())
        if sClean == sClean[::-1]:
            return True
        else: 
            return False