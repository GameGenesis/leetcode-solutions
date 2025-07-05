class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        print(nums)
        l, r = 0, 1
        maxLen = 0

        while r < len(nums):
            while l < r and nums[r] - nums[l] > 1:
                l += 1

            if nums[r] - nums[l] == 1:
                maxLen = max(maxLen, r - l + 1)
            r += 1
        
        return maxLen