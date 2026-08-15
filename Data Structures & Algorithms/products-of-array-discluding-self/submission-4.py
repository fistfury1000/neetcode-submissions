class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = (len(nums)) *[1]
        prefix = 1
        postfix=1
        for x in range(len(nums)):
            res[x] = prefix
            prefix *= nums[x]
        for j in range(len(nums)-1,-1,-1):
                res[j] *= postfix
                postfix *=nums[j]
        return res


        