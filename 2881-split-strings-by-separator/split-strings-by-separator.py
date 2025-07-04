class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        a=[]
        for w in words:
            if separator in w:
                b = w.split(separator)
                while '' in b:b.remove('')
                a.extend(b)
            else:
                a.append(w)

        return a