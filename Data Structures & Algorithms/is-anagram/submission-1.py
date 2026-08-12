class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n = len(s)
        m = len(t)

        if n != m:
            return False
        count_s = dict()
        count_t = dict()

        for i in range(n):
            count_s[s[i]] = count_s.get(s[i],0) + 1
            count_t[t[i]] = count_t.get(t[i],0) + 1

        return count_s == count_t
        
