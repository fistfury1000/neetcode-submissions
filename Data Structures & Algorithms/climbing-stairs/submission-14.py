class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1,1
        for x in range(0,n-1):
            temp = one
            one+=two
            two = temp
        return one
        