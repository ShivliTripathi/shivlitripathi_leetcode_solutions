class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        small=[]
        for i in range(len(nums)):
            l=list(map(int,str(nums[i])))
            if i == sum(l):
                small.append(i)
        
        if small:
            return small[0]
        return -1