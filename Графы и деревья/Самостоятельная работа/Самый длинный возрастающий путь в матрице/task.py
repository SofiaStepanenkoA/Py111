from typing import List


def longest_increasing_path(matrix: List[List[int]]) -> int:
    if not matrix:
        return 0

    m, n = len(matrix), len(matrix[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    dp = [[0] * n for _ in range(m)]
    ans = 0

    def dfs(i, j):
        if dp[i][j] != 0:
            return dp[i][j]
        max_length = 1
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj] > matrix[i][j]:
                length = 1 + dfs(ni, nj)
                max_length = max(max_length, length)

        dp[i][j] = max_length
        return max_length
    for i in range(m):
        for j in range(n):
            ans = max(ans, dfs(i, j))
    return ans