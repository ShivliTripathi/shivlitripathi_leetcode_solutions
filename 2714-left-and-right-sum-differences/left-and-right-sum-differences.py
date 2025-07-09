class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left,right = [],[]
        for i in range(len(nums)):
            if i==0:
                left.append(0)
            else:
                left.append(sum(nums[:i]))
        for j in range(len(nums)):
            if j== len(nums)-1:
                right.append(0)
            else:
                right.append(sum(nums[j+1:]))
                
        answer=[]
        for x,y in zip(left,right):
            answer.append(abs(x-y))
        return answer