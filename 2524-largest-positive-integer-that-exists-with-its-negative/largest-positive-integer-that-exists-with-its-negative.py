class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        a=[]
        for i in range(len(nums)):
            n=nums[i]
            if nums[i]>0 and -n in nums:
                a.append(nums[i])
                
        if a:
            return max(a)    
        return -1