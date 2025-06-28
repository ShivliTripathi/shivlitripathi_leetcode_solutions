class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        from collections import Counter
        x=Counter(nums)
        
        for val in x.values():
            if val<=1:
                continue
            if val==2:
                return True
            if val%2 == 0:
                continue
            prime= True
            for i in range(3, int(val**0.5) + 1, 2):
                if val%i == 0:
                    prime= False
                    break
            if prime:
                return True
        else:
            return False