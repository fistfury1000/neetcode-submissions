class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        poopMap = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in poopMap:
                return [poopMap[diff], i]
            poopMap[n] = i
        return

        