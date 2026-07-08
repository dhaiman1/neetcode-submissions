class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        new_array = []
        for i in range(len(nums)):
            product = 1
            for j in range(len(nums)):
                if i != j:
                    product *= nums[j]
            new_array.append(product)
        return new_array