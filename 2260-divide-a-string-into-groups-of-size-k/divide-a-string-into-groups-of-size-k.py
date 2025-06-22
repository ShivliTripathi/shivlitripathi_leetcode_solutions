class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        final=[]

        if len(s)%k==0:
            
            for i in range(0,len(s),k):
                final.append(s[i:i+k])
        else:
            r=len(s)%k
            remainder=s[-r:]
            s=s[:len(s)-r]
            
            for i in range(0,len(s),k):
                final.append(s[i:i+k])
                
            while r!=k:
                remainder+=fill
                r+=1
            final.append(remainder)

        return final