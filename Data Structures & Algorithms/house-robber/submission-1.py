class Solution:
    def rob(self, nums: List[int]) -> int:
        one = 0
        two = 0

        for n in nums:
            most = max(one + n, two)
            one = two
            two = most

        return two
