class Solution:
    def maxSum(self, nums: List[int]) -> int:

        even,odd =[],[]         
        for i in nums:
            if i>=0 and i not in even:
                even.append(i)

            elif i>=0 and i in even:
                continue

            elif i<0 and i not in odd:
                odd.append(i)

            else:
                continue

        if even:
            return sum(even)
        else:
            odd.sort()
            return odd[-1] 