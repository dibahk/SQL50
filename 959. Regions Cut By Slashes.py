class Solution(object):
    def regionsBySlashes(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        row, col = len(grid), len(grid[0])
        row2, col2 = 3 * row, 3 * col
        ngrid = [[0] * col2 for _ in range(row2)]
        for r in range(row):
            for c in range(col):
                rn, cn = 3 * r, 3 * c
                if grid[r][c] == '/':
                    ngrid[rn + 2][cn] = 1
                    ngrid[rn + 1][cn + 1] = 1
                    ngrid[rn][cn + 2] = 1
                if grid[r][c] == '\\':
                    ngrid[rn][cn] = 1
                    ngrid[rn + 1][cn + 1] = 1
                    ngrid[rn + 2][cn + 2] = 1
        def DFS(r, c, visited):
            if (r < 0 or c < 0 or r == row2 or c == col2 or ngrid[r][c] == 1 or (r, c) in visited):
                return
            visited.add((r, c))
            neighbors = [[r+1, c],[r, c+1],[r-1, c],[r, c-1]]
            for nr, nc in neighbors:
                DFS(nr, nc, visited)
        visited = set()
        ans = 0
        for r in range(row2):
            for c in range(col2):
                if ngrid[r][c] == 0 and (r, c) not in visited:
                    DFS(r, c, visited)
                    ans += 1
        return ans
