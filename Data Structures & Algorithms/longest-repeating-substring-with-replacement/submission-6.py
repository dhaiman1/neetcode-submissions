class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0 
        l = 0
        hash_map = {}
        top_freq = 0
        if not s: return res
        for r in range(len(s)):
            hash_map[s[r]] = 1 + hash_map.get(s[r], 0)
            top_freq = max(top_freq, hash_map[s[r]])
            if (r - l + 1) - top_freq > k:
                hash_map[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res