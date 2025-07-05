class Solution:
    def findLHS(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        
        freqMap = Counter(nums)
        maxLen = 0

        if len(freqMap) == 1:
            return 0

        for num, freq in freqMap.items():
            if (num - 1) in freqMap:
                maxLen = max(maxLen, freq + freqMap[num-1])
        
        return maxLen