class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:

        m=0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if abs(nums[i]-nums[j]) <= min(nums[i],nums[j]):
                    x = nums[i] ^ nums[j]
                    m= max(m,x)

        return m