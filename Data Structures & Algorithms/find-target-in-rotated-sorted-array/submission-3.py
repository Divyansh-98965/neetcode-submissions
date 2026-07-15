class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Brute Force
        # for i in range(len(nums)):
        #     if nums[i] == target:
        #         return i

        # return -1
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            # Case 1: The left half is perfectly sorted
            if nums[l] <= nums[mid]:
                # Check if the target is sitting inside this sorted left half
                if nums[l] <= target < nums[mid]:
                    r = mid - 1 
                else:
                    l = mid + 1
                    
            # Case 2: The right half must be perfectly sorted
            else:
                # Check if the target is sitting inside this sorted right half
                if nums[mid] < target <= nums[r]:
                    l = mid + 1  
                else:
                    r = mid - 1                    
        return -1