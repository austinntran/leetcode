from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        distributionToStrings = {}
        for string in strs:
            distribution = tuple(self.letterDist(string.lower()))
            arr = distributionToStrings.get(distribution, [])
            arr.append(string)
            distributionToStrings[distribution] = arr
        return list(distributionToStrings.values())

    def letterDist(self, s: str):
        fakeDict = [0] * 26
        for letter in s:

            fakeDict[ord(letter) - ord('a')] += 1
        return fakeDict