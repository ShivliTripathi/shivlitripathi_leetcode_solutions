class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        dic=[]
        for x,y in zip(names,heights):
            dic.append((x,y))
            
        return  [k for k,v in sorted(dic, key=lambda item: -item[1])]