class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        x=Counter(arr)
        a = ceil(len(arr)/4)
        for k,v in sorted(x.items(), key=lambda item: item[1], reverse=True):
            if v>=a:
                return k