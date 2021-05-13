# Connected components (DFS)
def numIslands(grid):
    if len(grid) == 0:
        return 0
    numOfIslands = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (grid[i][j] == '1'):
                numOfIslands += dfs(grid, i, j)
    return numOfIslands


def dfs(grid, i, j):
    if i < 0 or i >= len(grid) \
            or j < 0 or j >= len(grid[0]) \
            or grid[i][j] == '0':
        return 0
    grid[i][j] = '0'
    dfs(grid, i + 1, j)
    dfs(grid, i - 1, j)
    dfs(grid, i, j + 1)
    dfs(grid, i, j - 1)
    return 1


if __name__ == '__main__':
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    grid2 = [
        ["1", "1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    print("The number of islands is:", numIslands(grid2))


