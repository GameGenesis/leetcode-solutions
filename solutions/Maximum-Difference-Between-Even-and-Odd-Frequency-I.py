class Solution:
    def maxDifference(self, s: str) -> int:
        freq = Counter(s)
        odd = 0
        even = 100
        
        for val in freq.values():
            if val == 0: continue
            if val & 1:
                odd = max(odd, val)
            else:
                even = min(even, val)
        
        return odd - even