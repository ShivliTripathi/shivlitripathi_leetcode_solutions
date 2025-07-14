class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        w=''
        for i in words:
            w+=i
            if w==s:
                return True
        return False