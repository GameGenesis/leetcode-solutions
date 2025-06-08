class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []

        def dfs(num):
            if num and num > n: return

            if not num:
                for i in range(1, 10):
                    dfs(i)
                return

            res.append(num)

            for i in range(10):
                dfs(num*10+i)

        dfs(None)
        return res