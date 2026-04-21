class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_freq, max_len, i, j = 0, 0, 0, 0
        freq = list(0 for _ in range(26))
        size = len(s)

        while j < size:
            freq[ord(s[j]) - ord('A')] += 1
            max_freq = max(max_freq, freq[ord(s[j]) - ord('A')])
            if (j - i + 1) - max_freq <= k:
                max_len = max(max_len, j - i + 1)
            else:
                freq[ord(s[i]) - ord('A')] -= 1
                i+=1
            j+=1
        return max_len