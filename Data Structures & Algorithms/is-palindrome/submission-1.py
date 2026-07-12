class Solution:
    def isPalindrome(self, s: str) -> bool:
        reformat = ""
        for c in s:
            if c.isalnum():
                reformat += c
        
        reverse = ""
        for i in range(len(reformat) - 1, - 1, -1):
            reverse += reformat[i]
        
        if reverse.lower() == reformat.lower():
            return True
        return False

