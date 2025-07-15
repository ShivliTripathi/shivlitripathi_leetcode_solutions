class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        a=[]
        for ind,x in enumerate(nums):
            if ind%10 == x:
                a.append(ind)
            
        if a:
            return min(a)
        return -1