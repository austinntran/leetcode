class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False
        tDict = {}
        for letter in t:
            occurrences = tDict.get(letter, 0)
            tDict[letter] = occurrences + 1
        sDict = {}
        for letter in s:
            occurrences = sDict.get(letter, 1)
            if occurrences > tDict.get(letter, 0):
                return False
            sDict[letter] = occurrences + 1
        return True