class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(0, len(nums) - 2, 3):
            newArr = nums[i:i+3]
            largestDiff = newArr[-1] - newArr[0]
            if largestDiff > k:
                return []

            res.append(newArr)
        
        return res