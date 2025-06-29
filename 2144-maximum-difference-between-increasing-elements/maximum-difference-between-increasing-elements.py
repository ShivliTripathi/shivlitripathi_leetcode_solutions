class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        m=0

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]<nums[j]:
                    diff = nums[j]-nums[i]
                    m=max(m,diff)

        if m!=0:
            return m
        return -1