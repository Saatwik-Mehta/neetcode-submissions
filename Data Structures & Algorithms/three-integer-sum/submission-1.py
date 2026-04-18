class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        i = 0
        n = len(nums)
        op = []
        while i <= n-1:
            j = i+1
            k = n-1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s == 0:
                    op.append([nums[i], nums[j], nums[k]])
                    j+=1
                    while j < k and nums[j-1] == nums[j]:
                        j+=1
                    k-=1
                    while k >= 0 and nums[k+1] == nums[k]:
                        k-=1
                elif s > 0:
                    k-=1
                    while k >= 0 and nums[k+1] == nums[k]:
                        k-=1
                else:
                    j+=1
                    while j < k and nums[j-1] == nums[j]:
                        j+=1
            i+=1
            while i < n and nums[i-1] == nums[i]:
                i+=1
        return op
        