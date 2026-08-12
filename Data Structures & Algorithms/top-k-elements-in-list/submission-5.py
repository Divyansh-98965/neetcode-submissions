class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count frequencies - O(N)
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1
            
        # Step 2: Bucket array where index = frequency - O(N)
        # freq[i] stores a list of numbers that appear exactly 'i' times
        freq = [[] for _ in range(len(nums) + 1)]
        for num, c in count.items():
            freq[c].append(num)
            
        # Step 3: Iterate backwards from highest frequency bucket - O(N)
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res