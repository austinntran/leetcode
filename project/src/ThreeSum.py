from typing import List
class Solution:
    def Slow(self, nums: List[int]) -> List[List[int]]:
        occurrences = dict()
        threeRepeatMax = []
        for x in nums:
            val = occurrences.get(x, 0) + 1
            occurrences[x] = val
            if val < 4:
                threeRepeatMax.append(x)
        nums = sorted(threeRepeatMax)
        mapOfValues = dict()
        length = len(nums)
        for bi in range(length):
            valb = nums[bi]
            for ci in range(bi + 1, length):
                valc = nums[ci]
                combined = valb + valc
                tups = mapOfValues.get(combined, set())
                tups.add(tuple([valb, valc]))
                mapOfValues[combined] = tups
        ansSet = set()
        for ai in range(length):
            vala = nums[ai]
            options = mapOfValues.get(-vala, ())
            for tup in options:
                occurrences2 = dict()
                occurrences2[vala] = 1
                occurrences2[tup[0]] = occurrences2.get(tup[0], 0) + 1
                occurrences2[tup[1]] = occurrences2.get(tup[1], 0) + 1
                if occurrences2[vala] > occurrences[vala] or occurrences2[tup[0]] > occurrences[tup[0]] or occurrences2[tup[1]] > occurrences[tup[1]]:
                    continue
                ansSet.add(tuple(sorted([vala, tup[0], tup[1]])))

        return [[a, b, c] for (a, b, c) in ansSet]
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ans = []
        i = 0
        while i < len(nums):
            while i != 0 and i < len(nums) and nums[i] == nums[i - 1]:
                i += 1
            if i == len(nums):
                return ans
            j = i + 1
            k = len(nums) - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total == 0:
                    ans.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while nums[j - 1] == nums[j] and j < k:
                        j += 1
                elif total > 0:
                    k -= 1
                elif total < 0:
                    j += 1
            i += 1
        return ans