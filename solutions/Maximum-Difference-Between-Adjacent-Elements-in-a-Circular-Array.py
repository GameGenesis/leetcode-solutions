class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        maxDiff = abs(nums[0] - nums[-1])

        for num1, num2 in pairwise(nums):
            maxDiff = max(maxDiff, abs(num1 - num2))
        
        return maxDiff