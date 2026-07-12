class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        for i in range(len(heights)):
            for j in range(len(heights)):
                width = abs(j - i)
                height = min(heights[i], heights[j])
                area = width * height
                res = max(area, res)

        return res