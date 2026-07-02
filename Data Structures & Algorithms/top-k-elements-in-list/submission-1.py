class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        new_dict = {}
        for num in nums:
            new_dict[num] = 1 + new_dict.get(num, 0)
        new_list = []
        for key, value in new_dict.items():
            new_list.append([value, key])
        
        descending_list = sorted(new_list, reverse=True)

        final_list = []
        for i in range(k):
            final_list.append(descending_list[i][1])
        
        return final_list

