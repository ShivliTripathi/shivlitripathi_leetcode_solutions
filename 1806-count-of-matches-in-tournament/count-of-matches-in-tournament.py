class Solution:
    def numberOfMatches(self, n: int) -> int:
        m=[]
        a=0
        
        while n>1:
            if n%2==0:
                a= n//2
                m.append(a)
                n=a
            else:
                a=n//2
                m.append(a)
                n=(a+1)

        return sum(m)