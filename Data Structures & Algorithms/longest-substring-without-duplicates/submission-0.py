class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n  = len(s)
        maxl = 0
        for i in range(n):
            seen = set()
            for j in range(i, n):
                if s[j] not in seen:
                    seen.add(s[j])
                    maxl = max(maxl, j-i+1)
                else:
                    break
        return maxl
        


