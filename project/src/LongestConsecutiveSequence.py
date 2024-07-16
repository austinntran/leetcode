from typing import List
class Solution:
    def longestConsecutiveMemexceed(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        maxOfNums = max(nums)
        minOfNums = min(nums)
        rangeOfNums = maxOfNums - minOfNums + 1
        check = [False for _ in range(rangeOfNums)]
        for x in nums:
            check[x - minOfNums] = True
        longestChain = 0
        currentChain = 0
        for i in range(rangeOfNums):
            if check[i]:
                currentChain += 1
            else:
                currentChain = 0
            if currentChain > longestChain:
                longestChain = currentChain
        return longestChain
    
    def longestConsecutiveSlow(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        maxOfNums = max(nums)
        minOfNums = min(nums)
        setOfNums = set(nums)
        longestChain = 0
        currentChain = 1
        for i in range(minOfNums, maxOfNums + 1):
            if i in setOfNums and (i + 1) in setOfNums:
                currentChain += 1
            else: 
                currentChain = 1
            longestChain = max(currentChain, longestChain)
        return longestChain

    def longestConsecutive(self, nums: List[int]) -> int:
        setOfNums = set(nums)
        longestChain = 0
        currentChain = 0
        for i in nums:
            currentChain = 1
            if i - 1 not in setOfNums:
                while i + 1 in setOfNums:
                    currentChain += 1
                    i += 1
            longestChain = max(currentChain, longestChain)
        return longestChain