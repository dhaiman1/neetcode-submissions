class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if i != j and nums[i] + nums[j] == target:
        #             return [i, j]
        hash_map = dict()
        for i in range(len(nums)):
            needed = target - nums[i]
            if needed in hash_map:
                return[hash_map[needed], i]
            else:
                hash_map[nums[i]] = i

