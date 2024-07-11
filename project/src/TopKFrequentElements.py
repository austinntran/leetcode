from typing import List
class Solution:
    def topKFrequentSlow(self, nums: List[int], k: int) -> List[int]:
        frequencies = {}
        for n in nums:
            frequencies[n] = frequencies.get(n, 0) + 1
        sortedList = sorted(frequencies.items(), key = lambda item: item[1],  reverse = True)
        return [sortedList[i][0] for i in range(k)]
            
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numberToFrequency = {}
        for n in nums:
            numberToFrequency[n] = numberToFrequency.get(n, 0) + 1
        frequencyToNumber = [[] for _ in range((len(nums) + 1))]
        for key, val in numberToFrequency.items():
            frequencyToNumber[val].append(key)
        vals = []
        for x in range(len(frequencyToNumber) - 1, 0, -1):
            for number in frequencyToNumber[x]:
                vals.append(number)
                if len(vals) == k:
                    return vals
        return []