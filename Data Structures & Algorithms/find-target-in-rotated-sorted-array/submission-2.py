class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Brute Force
        # for i in range(len(nums)):
        #     if nums[i] == target:
        #         return i

        # return -1
        l = 0
        r = len(nums) - 1
        nums_len = len(nums)
        while True:
            mid = (l + r)//2
            if target == nums[mid]:
                return mid
            elif target in nums[l:mid + 1]:
                r = mid - 1
            elif target in nums[mid:r + 1]:
                l = mid + 1
            else:
                 return -1



        