class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        last = cost[-1]
        second_last = cost[len(cost) - 2]

        for i in range(len(cost) - 3, -1, -1):
            lowest_cost = cost[i] + min(second_last, last)
            last = second_last
            second_last = lowest_cost

        return min(second_last, last)