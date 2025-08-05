class Solution:
    def modifyString(self, s: str) -> str:
        import string
        alphabets = list(string.ascii_lowercase)

        for i in range(len(s)):
            for x in alphabets:
                if s[i]=='?' and x not in s[i+1:] and s[i-1]!=x:
                    s=s.replace('?',x,1)

        return s