class Solution:
    def containsDuplicate(self, nums) -> bool:
        l = 0
        s = set()
        for x in nums:
            if x in s:
                return True
            s.add(x)
        return False
