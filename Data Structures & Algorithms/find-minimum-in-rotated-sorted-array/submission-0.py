class Solution:
    def findMin(self, nums: List[int]) -> int:
        smallest = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < smallest:
                smallest = nums[i]
                break
        return smallest
        