class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # if not nums:
        #     return 0
        hash_set = set(nums)
        longest = 0
        for num in hash_set:
            sequence = 1
            if (num - 1) not in hash_set:
                next_num = num + 1
                while next_num in hash_set:
                    sequence += 1
                    next_num += 1
            longest = max(sequence, longest)
        
        return longest

        # numSet = set(nums)
        #         longest = 0

        #         for num in numSet:
        #             if (num - 1) not in numSet:
        #                 length = 1
        #                 while (num + length) in numSet:
        #                     length += 1
        #                 longest = max(length, longest)
        #         return longest
