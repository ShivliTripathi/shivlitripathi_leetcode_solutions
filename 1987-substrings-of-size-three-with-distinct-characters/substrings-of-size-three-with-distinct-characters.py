class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        
        a=''
        b=[]
        cnt=0
        for i in range(len(s)-2):
            a=s[i]+s[i+1]+s[i+2]
            b.append(a)
            
        for x in b:
            if len(x)==len(set(x)):
                cnt+=1
        
        return cnt