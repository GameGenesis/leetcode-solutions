class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freqMap = {}
        maxLucky = -1

        for elem in arr:
            freqMap[elem] = 1 + freqMap.get(elem, 0)
        
        for elem, freq in freqMap.items():
            if elem == freq:
                maxLucky = max(maxLucky, elem)
        
        return maxLucky