class Solution:
    def isValid(self, s: str) -> bool:
        hash_map = {')': '(', ']': '[', '}': '{'}
        stack = []
        for i in range(len(s)):
            if s[i] not in hash_map:
                stack.append(s[i])
            else:
                if stack and hash_map[s[i]] == stack[-1]:
                    stack.pop()
                else:
                    return False

        if stack == []:
            return True
        return False