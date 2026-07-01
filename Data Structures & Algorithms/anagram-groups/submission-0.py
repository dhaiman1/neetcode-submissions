class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}
        new_list = []
        for word in strs:
            key = "".join(sorted(word))
            if key in hash_map:
                hash_map[key].append(word)
            else:
                hash_map[key] = [word]
        
        for key in hash_map:
            new_list.append(hash_map[key])
        
        return new_list
        
        