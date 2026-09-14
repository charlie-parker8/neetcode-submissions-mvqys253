class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(nums):
            one = 0
            two = 0

            for n in nums:
                largest = max(one + n, two)
                one = two
                two = largest

            return two

        return max(nums[0], helper(nums[1:]), helper(nums[:-1]))