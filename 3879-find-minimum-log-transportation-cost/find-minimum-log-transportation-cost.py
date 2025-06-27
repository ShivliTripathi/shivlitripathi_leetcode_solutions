class Solution:
    def minCuttingCost(self, n: int, m: int, k: int) -> int:
        cost=0
        if n<=k and m<=k:
            cost=0
        else:
            if n>k:
                len1=k
                len2=n-k
                cost=len1*len2
            else:
                len1=k
                len2=m-k
                cost=len1*len2

        return cost