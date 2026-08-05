class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        remi = 0
        for x in nums:
            remi = remi^x
        return remi
        