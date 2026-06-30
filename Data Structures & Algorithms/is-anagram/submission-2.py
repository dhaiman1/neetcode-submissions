class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Solution 1
        # return sorted(s) == sorted(t)
        
        if len(s) != len(t):
            return False
        
        count_s, count_t = {}, {}
        for i in range(len(s)):
            count_s[s[i]] = 1 + count_s.get(s[i], 0)
            count_t[t[i]] = 1 + count_t.get(t[i], 0)
        
        for k in count_s:
            if count_s[k] != count_t.get(k):
                return False
        return True
            

        # my_dict = {}
        # for char in s:
        #     if char in my_dict:
        #         my_dict[char] += 1
        #     else:
        #         my_dict[char] = 1
        
        # for char in t:
        #     if char in my_dict:
        #         my_dict[char] -= 1
        #     else:
        #         return False
        
        # for key in my_dict:
        #     if my_dict[key] != 0:
        #         return False
        # return True
