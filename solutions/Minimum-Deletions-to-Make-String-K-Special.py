from collections import Counter

class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        freq = Counter(word)
        res = len(word)

        # choose a freq to base deletions off of
        for v in freq.values():
            deletions = 0
            # find # deletions for the selected elem freq
            for a in freq.values():
                if a < v:
                    deletions += a
                if a > v + k:
                    deletions += max(0, a - (v + k))
            # minimize the deletions
            res = min(res, deletions)
        
        return res
                
