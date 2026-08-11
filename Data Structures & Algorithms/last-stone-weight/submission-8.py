class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) >1:
            stones.sort()
            poop = stones.pop()-stones.pop()
            if poop:
                stones.append(poop)
        return stones[0] if stones else 0
        