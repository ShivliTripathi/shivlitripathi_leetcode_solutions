class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        dic={}
        for i in range(len(mat)):
            dic[i] = mat[i].count(1)

        d = sorted(dic.items(),key=lambda item:-item[1])
        return d[0]