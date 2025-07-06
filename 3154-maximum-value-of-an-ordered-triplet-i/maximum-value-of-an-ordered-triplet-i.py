class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        m=0

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    triplet = (nums[i]-nums[j]) * nums[k]
                    m = max(m,triplet)

        return m