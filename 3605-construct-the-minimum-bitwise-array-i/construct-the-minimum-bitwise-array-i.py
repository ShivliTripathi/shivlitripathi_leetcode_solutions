class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans=[]
        for x in nums:
            for y in range(x):
                if y | (y+1) == x:
                    ans.append(y)
                    break
            else:
                ans.append(-1)

        return ans