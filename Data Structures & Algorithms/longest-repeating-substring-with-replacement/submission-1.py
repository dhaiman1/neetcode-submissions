class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0 
        l = 0
        hash_map = {}
        for r in range(len(s)):
            hash_map[s[r]] = 1 + hash_map.get(s[r], 0)
            replace = (r - l + 1) - max(hash_map.values())
            while replace > k:
                hash_map[s[l]] -= 1
                l += 1
                replace = (r - l + 1) - max(hash_map.values())
            res = max(res, r - l + 1)
        return res