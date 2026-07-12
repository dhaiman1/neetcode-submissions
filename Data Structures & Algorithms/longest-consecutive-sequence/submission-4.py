class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # if not nums:
        #     return 0
        hash_set = set(nums)
        longest = 0
        for num in hash_set:
            curr = num
            sequence = 1
            if (curr - 1) not in hash_set:
                while curr + 1 in hash_set:
                    sequence += 1
                    curr += 1
            longest = max(sequence, longest)
        
        return longest