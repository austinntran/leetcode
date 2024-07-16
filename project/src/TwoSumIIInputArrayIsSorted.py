from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        pairToIndex = dict()
        for i in range(len(numbers)):
            opposite = target - numbers[i]
            indexOfSelf = pairToIndex.get(numbers[i], -1)
            if indexOfSelf != -1:
                return sorted([i + 1, indexOfSelf + 1])
            pairToIndex[opposite] = i