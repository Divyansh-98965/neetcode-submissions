class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # hash set approach
        # seen = set()
        n = len(nums)
        # for i in range(n):
        #     if nums[i] in seen:
        #         return nums[i]
        #     else:
        #         seen.add(nums[i])
        # return -1

        # two pointer approach
        # You are given an array of integers nums containing
        # n + 1 integers. Each integer in nums is in the range [1, n] inclusive
        slow = nums[0]    
        fast = nums[0]

        while True:
            # detecting cycle in the array
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow2 = nums[0]

        while slow2 != slow:
            slow2 = nums[slow2]
            slow = nums[slow]

        return slow
