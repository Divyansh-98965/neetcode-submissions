class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #brute force solution
        k = 1 
        n = len(nums)
        res = [1] * n
        prefix_array = [1] * n 
        suffix_array = [1] * n

        for i in range(1,n):
            prefix_array[i] = nums[i - 1] * prefix_array[i - 1]
        
    
        # Loop backwards: element at i depends on what is to its right
        for i in range(n - 2, -1, -1):
            suffix_array[i] = suffix_array[i + 1] * nums[i + 1]
        
        for i in range(n):
            res[i] = prefix_array[i] * suffix_array[i]
        
        return res
