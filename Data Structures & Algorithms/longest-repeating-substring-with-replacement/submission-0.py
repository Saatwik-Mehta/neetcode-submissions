class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # frq of the most occuring character
        max_frq = 0
        # length of the valid substring
        max_len = 0
        size = len(s)
        for i in range(size):
            # character frequence will be stored in the array
            char_frq = list(0 for i in range (26))
            for j in range(i, size):
                # find the correct index of the current character
                # by substracting the ord(char) from ord('A')
                char_frq[ord(s[j]) - ord('A')] += 1
                # Now, compare the current character frequency with the max_frq
                max_frq = max(max_frq, char_frq[ord(s[j]) - ord('A')])
                # find, how many characters to be changed for the given max_frq of the charcter
                change = (j - i + 1) - max_frq
                # if the change is within the allowed replacement k, then we can take the length of that substring as a valid length
                if change <= k:
                    max_len = max(max_len, j - i + 1)
                else: break
        return max_len