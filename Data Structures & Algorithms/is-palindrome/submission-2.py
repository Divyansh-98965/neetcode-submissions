class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = s.strip().lower()

        clean_text = "".join([char for char in s1 if char.isalnum()])
        
        for i in range(len(clean_text)//2):
            n = len(clean_text)
        
            if clean_text[i] != clean_text[n - i - 1]:
                return False
        
        return True
        