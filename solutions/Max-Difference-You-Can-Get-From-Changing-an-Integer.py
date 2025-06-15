class Solution:
    def maxDiff(self, num: int) -> int:
        a = b = str(num)

        # Find left-most digit that isn't a 9 and replace all occurances with 9
        for digit in a:
            if digit != "9":
                a = a.replace(digit, "9")
                break
        
        # Check if leading isn't 1 and replace with 1 (no leading 0)
        if b[0] != "1":
            b = b.replace(b[0], "1")
        else:
            # Find leading digit that isn't 1 or 0
            # We can't replace 1 since leading 1 would turn into leading 0
            for digit in b[1:]:
                if digit != "0" and digit != "1":
                    b = b.replace(digit, "0")
                    break
        
        return int(a) - int(b)

        