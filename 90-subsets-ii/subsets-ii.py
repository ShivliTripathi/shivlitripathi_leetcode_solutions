class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        import itertools

        subset=[]

        for x in range(len(nums)+1):
            subset.extend(itertools.combinations(nums, x))
        subset = set(tuple(sorted(s)) for s in set(subset))
        
        return [list(s) for s in list(subset)]