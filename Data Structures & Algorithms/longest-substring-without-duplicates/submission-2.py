class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        i = 0
        j = 0
        hashset = set()
        maxl = 0
        while j < n:
            if s[j] not in hashset:
                hashset.add(s[j])
                maxl = max(maxl, j - i + 1)
                j += 1
            else:
                hashset.remove(s[i])  # shrink window from left
                i += 1
        return maxl