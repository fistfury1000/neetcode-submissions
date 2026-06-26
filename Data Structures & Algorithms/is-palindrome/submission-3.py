class Solution:
    def isPalindrome(self, s: str) -> bool:
        newS = ''
        for x in s:
            if x.isalnum():
                newS += x.lower()
        return newS == newS[::-1]
        