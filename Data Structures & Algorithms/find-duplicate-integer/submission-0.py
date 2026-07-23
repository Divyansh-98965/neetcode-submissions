class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            curr_num = nums[i]
            if curr_num in nums[i + 1:n]:
                return curr_num

        return -1
        