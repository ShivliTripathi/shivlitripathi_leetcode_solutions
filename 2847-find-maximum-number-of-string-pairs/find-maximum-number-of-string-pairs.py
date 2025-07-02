class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        dic={}
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if words[i][::-1] == words[j]:
                    dic[words[i]]=words[j]

        return len(dic)