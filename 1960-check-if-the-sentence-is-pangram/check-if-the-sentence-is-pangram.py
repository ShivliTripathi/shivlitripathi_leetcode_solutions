class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabests='abcdefghijklmnopqrstuvwxyz'
        sentence = ''.join(list(sorted(set(sentence))))

        return  alphabests == sentence