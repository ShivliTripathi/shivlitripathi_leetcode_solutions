class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        import math
        nums.sort(reverse=True)
        prod1= math.prod(nums[:3])
        prod2= math.prod(nums[-2:]+[nums[0]])
        return max(prod1,prod2)