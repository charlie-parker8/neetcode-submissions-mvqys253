class Solution:
    def jump(self, nums: List[int]) -> int:
        count_windows = 0
        l = 0
        r = 0

        while r < len(nums) - 1:
            temp = 0
            for i in range(l, r + 1):
                temp = max(temp, i + nums[i])

            l = r + 1
            r = temp
            count_windows += 1

        return count_windows