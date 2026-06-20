class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_length = 0
        window_set = set()
        
        for right in range(len(s)):
            # If we hit a duplicate, shrink the left side UNTIL the duplicate is gone
            while s[right] in window_set:
                window_set.remove(s[left])
                left += 1
                
            # Now that the window is guaranteed clean, add the current character
            window_set.add(s[right])
            
            # Update our record holder
            max_length = max(max_length, (right - left) + 1)
            
        return max_length