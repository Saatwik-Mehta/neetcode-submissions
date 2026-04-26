class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #your code goes here
        if len(s) < len(t):
            return ""
        i, j, min_wind_str, flag, t_map, s_map = 0, 0, "", False, {}, {}
        for c in t:
            t_map[c] = (1 + t_map.get(c, 0))
        while j < len(s) and s[j] not in t_map:
            j+=1
            i+=1
        while j < len(s):
            s_map[s[j]] = (1 + s_map.get(s[j], 0))
            for c in t_map:
                if t_map[c] > s_map.get(c, 0):
                    flag = False
                    break
                flag = True
            if flag:
                min_wind_str = s[i: j+1] if len(min_wind_str) > len(s[i: j+1]) or not min_wind_str else min_wind_str
                s_map[s[i]] -=1
                i+=1
                s_map = {}
                while i < len(s) and s[i] not in t_map:
                    i+=1
                j = i
            else:
                j+=1
        return min_wind_str
Solution().minWindow("ADOBECODEBANC", "ABC")