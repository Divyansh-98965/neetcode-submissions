class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1 = nums1 + nums2
        nums1 = sorted(nums1)
        left = 0
        right = len(nums1) - 1

        if len(nums1)%2 == 0:
            half = left + ((left - right)//2)
            return (nums1[half] + nums1[half - 1])/2

        half = left + ((left - right)//2)
        return nums1[half - 1]