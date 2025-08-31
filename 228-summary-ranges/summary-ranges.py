class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        b=[]

        if len(nums)==0:
            return[]
        a = [nums[0]]  
        for i in range(1, len(nums)):
            if nums[i-1] + 1 == nums[i]:
                a.append(nums[i])
            else:
                b.append(set(a))
                a = [nums[i]]
        
        if a:
            b.append(set(a))

        c=[]
        for i in b:
            if len(i)>1:
                c.append(str(min(i))+"->"+str(max(i)))
            else:
                c.append(str(max(i)))
        return c