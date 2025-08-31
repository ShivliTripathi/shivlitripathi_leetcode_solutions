class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        from itertools import permutations

        seq=set()

        for i in range(1, len(tiles)+1):
            for p in permutations(tiles, i):
                seq.add(''.join(p))

        return len(seq)