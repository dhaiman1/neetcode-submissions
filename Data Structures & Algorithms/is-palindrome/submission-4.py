class Solution:
    def isPalindrome(self, s: str) -> bool:
        reformat = ""
        for c in s:
            if c.isalnum():
                reformat += c.lower()
        
        return reformat == reformat[::-1]

