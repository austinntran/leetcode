from typing import List
class Solution:
    def productExceptSelf2(self, nums: List[int]) -> List[int]:
        length = len(nums)
        left = [0 for _ in range(length)]
        right= [0 for _ in range(length)]
        ans = [0 for _ in range(length)]
        
        left[0] = nums[0]
        right[-1] = nums[-1]
        for x in range(1, length):
            left[x] = nums[x] * left[x - 1]
        for x in range(length - 2, -1, -1):
            right[x] = nums[x] * right[x + 1]
        ans[0] = right[1]
        ans[-1] = left[-2]
        for x in range(1, length - 1):
            ans[x] = left[x - 1] * right[x + 1]
        return ans
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        ans = [1 for _ in range(length)]
        acc = 1
        for x in range(0, length):
            ans[x] *= acc
            acc *=  nums[x]
        acc = 1
        for x in range(length - 1, -1, -1):
            ans[x] *= acc
            acc *= nums[x]
        return ans