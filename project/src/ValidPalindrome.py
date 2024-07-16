import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars = string.ascii_lowercase + string.digits
        filtered = ''
        reversed = ''
        for letter in s.lower():
            if letter in chars:
                filtered += letter
                reversed = letter + reversed
        return filtered == reversed