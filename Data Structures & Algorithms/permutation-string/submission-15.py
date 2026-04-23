class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        cnt1 = [0 for _ in range(26)]
        cnt2 = [0 for _ in range(26)]

        for i in range(len(s1)):
            cnt1[ord(s1[i]) - ord('a')] += 1
            cnt2[ord(s2[i]) - ord('a')] += 1
        match = sum(1 if cnt1[i] == cnt2[i] else 0 for i in range(len(cnt2)))

        if match==26:
            return True

        l = 0
        r = len(s1)
        while r < len(s2):
            index = ord(s2[r]) - ord('a')
            
            cnt2[index] += 1
            if cnt2[index] == cnt1[index]:
                match += 1
            elif cnt2[index] - 1 == cnt1[index]:  # was equal before increment
                match -= 1

            if match==26:
                return True
            index = ord(s2[l]) - ord('a')
            cnt2[index] -= 1
            if cnt2[index] == cnt1[index]:
                match += 1
            elif cnt2[index] + 1 == cnt1[index]:  # was equal before increment
                match -= 1 
           
            if match==26:
                return True
            r+=1
            l+=1
        return False
    
