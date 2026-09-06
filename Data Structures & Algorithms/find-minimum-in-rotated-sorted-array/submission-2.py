class Solution:
    def findMin(self, nums: List[int]) -> int:
        stack = []
        for num in nums:
            if not stack or num > stack[-1]:
                stack.append(num)
            else:
                return num
        return stack[0]
            