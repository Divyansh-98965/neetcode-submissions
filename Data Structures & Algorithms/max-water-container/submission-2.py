class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # #brute force approach 

        #area = 0
        # for i in range(len(heights)):
        #     for j in range(len(heights)):
        #         dummy_area = (j - i)*(min(heights[i], heights[j]))

        #         area = max(dummy_area, area)

        # return area

        # optimized approach 
        #area = heights[key1] - heights[key2]
        area = 0
        left = 0
        right = len(heights) - 1
        for i in range(len(heights)):
            dummy_area = (right - left) * min(heights[left], heights[right])
            area = max(dummy_area, area)

            if heights[left] >= heights[right]:
                right -= 1

            elif heights[left] <= heights[right]:
                left +=1

            elif right == left:
                break

        return area