class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        t_charfrq_map = {}
        substring_found = False
        minimum_windows = ""

        for i in range(len(t)):
            t_charfrq_map[t[i]] = (1 + t_charfrq_map.get(t[i], 0))
        
        for i in range(len(s)):
            s_charfrq_map = {}
            if s[i] not in t_charfrq_map:
                continue
            for j in range(i, len(s)):
                s_charfrq_map[s[j]] = (1 + s_charfrq_map.get(s[j], 0))
                for k in t_charfrq_map:
                    if (t_charfrq_map[k] > s_charfrq_map.get(k, 0)):
                        substring_found = False
                        break
                    substring_found = True
                if substring_found:
                    minimum_windows = s[i:j+1] if not minimum_windows else minimum_windows if len(minimum_windows) < len(s[i:j+1]) else s[i:j+1]
                    break
        return minimum_windows