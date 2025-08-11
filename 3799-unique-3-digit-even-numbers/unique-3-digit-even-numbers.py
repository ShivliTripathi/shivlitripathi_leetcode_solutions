class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        unique=set()
        for i in range(len(digits)):
            for j in range(len(digits)):
                for k in range(len(digits)):
                    if i==j or j==k or i==k:
                        continue
                    else:
                        n = str(digits[i])+str(digits[j])+str(digits[k])
                        x=int(n)
                        if len(str(x))==3 and n[0]!=0 and x%2==0:
                            unique.add(x)
    
        return len(unique)