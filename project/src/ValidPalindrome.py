import string
class Solution:
    def isPalindromeSlow(self, s: str) -> bool:
        chars = string.ascii_lowercase + string.digits
        filtered = ''
        reversed = ''
        for letter in s.lower():
            if letter in chars:
                filtered += letter
                reversed = letter + reversed
        return filtered == reversed
    def isPalindromeLessSlow(self, s: str) -> bool:
        s = s.lower()
        backwards = len(s) - 1
        forwards = 0
        while forwards < backwards:
            forwardLetter = s[forwards]
            backwardLetter = s[backwards]
            if not self.validChar(forwardLetter):
                forwards += 1
                continue
            if not self.validChar(backwardLetter):
                backwards -= 1
                continue
            if forwardLetter != backwardLetter:
                return False
            else:
                forwards += 1
                backwards -= 1
                
        return True
    
    def isPalindromeFaster(self, s: str) -> bool:
        s = s.lower()
        backwards = len(s) - 1
        forwards = 0
        while forwards < backwards:
            forwardLetter = s[forwards]
            backwardLetter = s[backwards]
            while not self.validChar(forwardLetter) and forwards < backwards:
                forwards += 1
                forwardLetter = s[forwards]
            while not self.validChar(backwardLetter) and forwards < backwards:
                backwards -= 1
                backwardLetter = s[backwards]
            if forwards == backwards:
                return True
            if forwardLetter != backwardLetter:
                return False
            else:
                forwards += 1
                backwards -= 1
        return True
    def validChar(self, c) -> bool:
        return c >= 'A' and c <= 'Z' or c >= 'a'and c <= 'z' or c >= '0' and c <= '9'
    
    def isPalindrome(self, s: str) -> bool:
        s = [char for char in s.lower() if char.isalnum()]
        return all(s[i] == s[~i] for i in range(len(s)//2))