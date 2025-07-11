class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        perm=0
        for x in s:
            if x in t:
                perm += abs(s.index(x) - t.index(x))
        return perm