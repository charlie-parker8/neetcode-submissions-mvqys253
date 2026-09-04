class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(r, c):
            if (r,c) in seen or r >= len(grid) or r < 0 or c >= len(grid[0]) or c < 0 or grid[r][c] != "1":
                return

            seen.add((r,c))

            directions = ((0,1), (0,-1), (1,0), (-1,0))

            for a, b in directions:
                dfs(r + a, c + b)

            return

        res = 0
        seen = set()

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (r,c) not in seen and grid[r][c] == "1":
                    dfs(r, c)
                    res += 1

        return res
        