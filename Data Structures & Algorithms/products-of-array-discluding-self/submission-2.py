class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # new_array = []
        # for i in range(len(nums)):
        #     product = 1
        #     for j in range(len(nums)):
        #         if i != j:
        #             product *= nums[j]
        #     new_array.append(product)
        # return new_array
        pre, post, res, prod = [], [], [], 1

        for i in range(len(nums)):
            pre.append(prod)
            prod *= nums[i]
        prod = 1
        for i in range(len(nums) -1, -1, -1):
            post.append(prod)
            prod *= nums[i]
        post.reverse()
        for i in range(len(nums)):
            final = pre[i] * post[i]
            res.append(final)
        
        return res
