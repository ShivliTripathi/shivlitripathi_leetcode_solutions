class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        import string
        alphabet = list(string.ascii_lowercase)
        #print(alphabet)

        dic={}
        for i,char in enumerate(s):
            if char.lower() in alphabet:
                dic[i] = char
        print(dic)

        key=[]
        val=[]
        for x,y in sorted(dic.items()):
            key.append(x)
            val.append(y)

        s=list(s)
        val = val[::-1]
        for k,v in zip(key,val):
            s[k]=v

        return ''.join(s)