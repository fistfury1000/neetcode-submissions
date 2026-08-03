class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        rem = 0
        for n in nums:
            rem = n^rem
        return rem
        