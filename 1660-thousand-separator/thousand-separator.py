class Solution:
    def thousandSeparator(self, n: int) -> str:
        l=list(str(n))
        a,b = [],[]

        if len(l)%3 ==0:
            for i in l[::-1]:
                a.insert(0,i)
                if len(a)==3:
                    b.insert(0,'.'+''.join(a))
                    a=[]
                    
            b=''.join(b)
            if b[0]=='.':
                b=b.replace(b[0],'',1)
        else:
            for i in l[::-1]:
                a.insert(0,i)
                if len(a)==3:
                    b.insert(0,'.'+''.join(a))
                    a=[]
                    
            if len(l)%3==1:
                b=l[0]+''.join(b)
            elif len(l)%3==2:
                b=l[0]+l[1]+''.join(b) 

        return b