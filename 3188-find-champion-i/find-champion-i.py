class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:

        dic={}
        for i in range(len(grid)):
            dic[i] = grid[i].count(1)

        
        key = [k for k,v in (sorted(dic.items(), key=lambda item:-item[1]))]
        return key[0]