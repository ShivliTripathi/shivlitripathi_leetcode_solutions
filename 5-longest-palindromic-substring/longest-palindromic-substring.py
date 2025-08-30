class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        a=''
        dic={}
        for i in range(len(s)):
            a=s[i]
            if a==a[::-1]:
                dic[a]=len(a)
            for j in range(i+1,len(s)):
                a+=s[j]
                if a == a[::-1]:
                    dic[a]=len(a)

        dic_sorted = sorted(dic.items(), key=lambda item: item[1],reverse=True)
        key=[k for k,v in dic_sorted]

        return key[0]