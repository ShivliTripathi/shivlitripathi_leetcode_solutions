class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                b = bin(nums[i] | nums[j])[2:]
                if b[-1] =='0':
                    return True
        return False