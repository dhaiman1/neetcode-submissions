class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # hash_set = set()
        # streak, longest = 0, 0
        # for c in s:
        #     if c in hash_set:
        #         hash_set = {c}
        #         streak = 1
        #     else:
        #         hash_set.add(c)
        #         streak += 1
        #     longest = max(streak, longest)
        
        # return longest

        # longest = 0
        # for i,c in enumerate(s):
        #     curr_s = s[i:]
        #     streak = 0
        #     hash_set = set()
        #     for j in curr_s:
        #         if j in hash_set:
        #             hash_set = {j}
        #             streak = 1
        #         else:
        #             hash_set.add(j)
        #             streak += 1
        #         longest = max(streak, longest)
        # return longest

        hash_set = set()
        longest = 0
        left = 0
        for right, c in enumerate(s):
            while s[right] in hash_set:
                hash_set.remove(s[left])
                left += 1
            streak = (right - left) + 1
            hash_set.add(s[right])
            longest = max(streak, longest)

        return longest
