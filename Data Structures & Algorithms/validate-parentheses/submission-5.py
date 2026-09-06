class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        h_m = {')': '(', ']': '[', '}': '{'}
        for c in s:
            if stack and c in h_m:
                if h_m[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False
