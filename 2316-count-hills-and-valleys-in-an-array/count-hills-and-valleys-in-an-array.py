class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        t,cnt=0,0
        for i in range(1,len(nums)):
            if nums[i-1]< nums[i]:
                if t==-1:
                    cnt+=1
                t=1
            elif nums[i-1] > nums[i]:
                if t==1:
                    cnt+=1
                t=-1
        return cnt