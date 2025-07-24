class Solution:
    def checkDivisibility(self, n: int) -> bool:
        import math

        l = list(map(int,str(n)))
        s = sum(l)
        p = math.prod(l)
        if n % (s+p) == 0:
            return True
        return False