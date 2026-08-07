class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        s = {}

        for i in range(n):
            x = target - nums[i]
            if x in s:
                return [s[x], i]
            s[nums[i]] = i
             