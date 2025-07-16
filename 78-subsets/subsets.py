class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        import itertools

        subset=[]

        for x in range(len(nums)+1):
            subset.extend(itertools.combinations(nums, x))
            print(subset)
        
        return [list(s) for s in subset]