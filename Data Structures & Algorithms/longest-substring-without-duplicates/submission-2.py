class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        for i,c in enumerate(s):
            curr_s = s[i:]
            streak = 0
            hash_set = set()
            for j in curr_s:
                if j in hash_set:
                    hash_set = {j}
                    streak = 1
                else:
                    hash_set.add(j)
                    streak += 1
                longest = max(streak, longest)
        return longest