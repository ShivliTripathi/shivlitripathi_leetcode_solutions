class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        for middleIndex in range(len(nums)):
            left = sum(nums[:middleIndex])
            right = sum(nums[middleIndex+1:])
            if left == right:
                return middleIndex

        return -1