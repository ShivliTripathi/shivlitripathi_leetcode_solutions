class Solution:
    def isValid(self, word: str) -> bool:

        vowels = any(c for c in word if c.lower() in ['a','e','i','o','u'])
        con = any(c for c in word if c.lower() not in ['a','e','i','o','u'] and c.isalpha())

        return len(word) >= 3 and word.isalnum() and vowels and con