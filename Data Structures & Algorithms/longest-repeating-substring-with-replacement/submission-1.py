class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len, max_freq, i, j = 0, 0, 0, 0
        size = len(s)
        freq = list(0 for _ in range(26))

        while j < size:
            freq[ord(s[j]) - ord('A')] += 1
            max_freq = max(max_freq, freq[ord(s[j]) - ord('A')])

            while (j - i + 1) - max_freq > k:
                freq[ord(s[i]) - ord('A')] -= 1
                max_freq = max(freq)
                i += 1
            max_len = max(max_len, j - i + 1)
            j += 1
        return max_len

