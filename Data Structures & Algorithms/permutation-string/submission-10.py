class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        # Build a hash of s1 to cnt the number of character to be checked in s2
        cnt1 = [0 for _ in range(26)]

        for i in range(len(s1)):
            cnt1[ord(s1[i])-ord('a')] += 1
        # Count distinct characters AFTER building cnt1
        need = sum(1 for x in cnt1 if x > 0)
        # Checking the length of the substring in s1 that should be present in s2

        for i in range(len(s2)):
            cur = 0
            # progressively building cnt2 for s2 to check the permutation s1 in s2
            cnt2 = [0 for _ in range(26)]
            for j in range(i, len(s2)):
                cnt2[ord(s2[j])-ord('a')] += 1
                # If the char freq in s2 exceeded from s1, break
                if cnt2[ord(s2[j])-ord('a')] > cnt1[ord(s2[j])-ord('a')]:
                    break
                if cnt2[ord(s2[j])-ord('a')] == cnt1[ord(s2[j])-ord('a')]:
                    cur+=1
                if need == cur:
                    return True
        return False
                