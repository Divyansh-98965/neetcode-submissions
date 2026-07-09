class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        right = len(s1)

        for i in range(len(s2)):
            substr = sorted(s2[left:right])
            if substr == sorted(s1):
                return True
            left += 1
            right += 1

        return False 