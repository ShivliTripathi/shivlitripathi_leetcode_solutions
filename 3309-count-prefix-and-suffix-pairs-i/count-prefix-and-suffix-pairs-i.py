class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:

        cnt=0

        for i in range(len(words)):
            for j in range(1,len(words)):
                if i<j and words[j].startswith(words[i]) and words[j].endswith(words[i]):
                    cnt+=1

        return cnt