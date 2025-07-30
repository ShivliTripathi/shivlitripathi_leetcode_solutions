class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        from itertools import chain, combinations
        import functools
        import operator

        subsets = list(chain.from_iterable(combinations(nums, r) for r in range(len(nums)+1)))

        subsets = [list(sub) for sub in subsets]

        s=0
        for x in subsets[1:]:
            s+= functools.reduce(operator.xor, x)
    
        return s