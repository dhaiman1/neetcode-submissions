class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # res = 0
        # for i in range(len(heights)):
        #     for j in range(len(heights)):
        #         width = abs(j - i)
        #         height = min(heights[i], heights[j])
        #         area = width * height
        #         res = max(area, res)

        # return res

        res = 0
        left, right = 0, len(heights) - 1
        while left < right:
            width = abs(right - left)
            height = min(heights[left], heights[right])
            area = width * height
            res = max(area, res)
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        return res
        