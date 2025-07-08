class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        a,dic=[],{}
        a.extend(arr)
        a = list(set(a))
        a.sort()

        for i,x in enumerate(a):
            if x not in dic.keys():
                dic[x] = i+1
        

        for j in range(len(arr)):
            arr[j]=dic[arr[j]]

        return arr