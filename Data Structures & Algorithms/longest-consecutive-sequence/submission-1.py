class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums1 = set(nums)
        count = 0
        sizearray = []
        for num in (nums1):
            # if nums - 1 is not in the set then it is a starting element
            if num - 1 not in nums1:
                start = num
                current_streak = 1
                # build streak
                while (start + 1) in nums1:
                    start += 1
                    current_streak += 1

                count = (max(count, current_streak))

        return count