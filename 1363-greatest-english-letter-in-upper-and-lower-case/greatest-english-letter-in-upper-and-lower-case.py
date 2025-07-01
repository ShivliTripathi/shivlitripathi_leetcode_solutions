class Solution:
    def greatestLetter(self, s: str) -> str:
        a=set()
        for x in s:
            if x.lower() in s and x.upper() in s:
                a.add(x.upper())
        st = sorted(a, reverse=True)
        if st:
            return st[0]
        return ""
        