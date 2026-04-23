class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        # Build a hashmap of s1 to cnt the number of character to be checked in s2
        cnt1 = {}

        for i in range(len(s1)):
            if s1[i] not in cnt1:
                cnt1[s1[i]] = 1
            else:
                cnt1[s1[i]] += 1
        
        need = len(cnt1)
        # Checking the length of the substring in s1 that should be present in s2

        for i in range(len(s2)):
            cur = 0
            # progressively building cnt2 for s2 to check the permutation s1 in s2
            cnt2 = {}
            for j in range(i, len(s2)):
                if s2[j] not in cnt2:
                    cnt2[s2[j]] = 1
                else:
                    cnt2[s2[j]] += 1
                # If the char freq in s2 exceeded from s1, break
                if cnt2[s2[j]] > cnt1.get(s2[j], 0):
                    break
                if cnt2[s2[j]] == cnt1.get(s2[j], 0):
                    cur+=1
                if need == cur:
                    return True
        return False
                