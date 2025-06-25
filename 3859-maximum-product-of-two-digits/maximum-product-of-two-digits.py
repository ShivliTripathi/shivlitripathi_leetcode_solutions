class Solution:
    def maxProduct(self, n: int) -> int:
        prod=1
        l=list(map(int,str(n)))
        l.sort(reverse=True)
        print(l)
        for i in range(2):
            prod*=l[i]

        return prod