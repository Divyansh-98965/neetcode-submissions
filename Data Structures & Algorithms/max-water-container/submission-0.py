class Solution:
    def maxArea(self, heights: List[int]) -> int:

        area = 0
        #brute force approach 
        for i in range(len(heights)):
            for j in range(len(heights)):
                dummy_area = (j - i)*(min(heights[i], heights[j]))

                area = max(dummy_area, area)

        return area