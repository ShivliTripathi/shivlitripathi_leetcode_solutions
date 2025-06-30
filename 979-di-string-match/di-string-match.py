class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        d,i = len(s),0
        a=[]
        perm=[]
        for x in range(len(s)):
            if s[x]=='I' and s[x] not in a:
                i=0
                perm.append(i)
                a.append('I')

            elif s[x]=='I' and s[x] in a:
                i+=1
                perm.append(i)

            elif s[x]=='D' and s[x] not in a:
                d=len(s)
                perm.append(d)
                a.append('D')

            elif s[x]=='D' and s[x] in a:
                d-=1
                perm.append(d)

        for y in range(len(s)+1):
            if y not in perm:
                perm.append(y)

        return perm