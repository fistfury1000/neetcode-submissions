class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        poop = len(nums)
        for x in range(len(nums)):
            for j in range(len(nums)):
                if nums[x] == nums[j]:
                    count +=1
                    if count > (len(nums)/2):
                        return nums[x]

        