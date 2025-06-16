class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        maxDiff = -1
        l, r = 0, 1
        
        while r < len(nums):
            if nums[l] < nums[r]:
                maxDiff = max(maxDiff, nums[r] - nums[l])
            if nums[r] < nums[l]:
                l = r
            r += 1

        return maxDiff