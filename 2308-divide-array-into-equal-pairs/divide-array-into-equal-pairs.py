class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        n = len(nums)/2
        x=Counter(nums)

        a=[]
        for i,j in x.items():
            if j%2 == 0:
                a.append(True)
            else:
                a.append(False)

        if False in a:
            return False
        return True