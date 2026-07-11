class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ''
        for x in s:
            if x.isalnum():
                newStr += x.lower()
        return newStr == newStr[::-1]