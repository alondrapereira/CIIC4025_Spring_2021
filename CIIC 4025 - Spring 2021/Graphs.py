import math

# *************** BFS (undirected) *************** #
def bfs(graph, source):
    queue = []
    for k, v in graph.items():
        graph[k] = {}
        if k == source:
            graph[k]["color"] = "GRAY"
            graph[k]["distance"] = 0
        else:
            graph[k]["color"] = "WHITE"
            graph[k]["distance"] = math.inf
        graph[k]["pi"] = "NIL"
        graph[k]["neighbours"] = v

    queue.append(source)
    while len(queue) > 0:
        current = queue.pop(0)
        for n in graph[current]["neighbours"]:
            if(graph[n]["color"] == "WHITE"):
                graph[n]["color"] = "GRAY"
                graph[n]["distance"] = graph[current]["distance"] + 1
                graph[n]["pi"] = current
                queue.append(n)
        graph[current]["color"] = "BLACK"

    return graph

# Test
g = {
    's' : {'t':6, 'y':7},
    't' : {'x':5, 'z':-4, 'y':8 },
    'y' : {'z':9, 'x':-3},
    'z' : {'x':7, 's': 2},
    'x' : {'t':-2}
}
# result = bfs(g,'s')

# ********* Shortest Path ********* #

def print_path(graph, fromNode, toNode):
    if fromNode == toNode:
        print(fromNode)
    elif graph[toNode]["pi"] == "NIL":
        print("No path from" + fromNode + " to " + toNode + " exists.")
    else:
        print_path(graph, fromNode, graph[toNode]["pi"])
        print(toNode)

# Test
# print_path(result, "s", "x")

# ********* Connected components (undirected) ********* #

# *************** DFS *************** #
def dfs(graph):
    for k, v in graph.items():
        graph[k] = {}
        graph[k]["color"] = "WHITE"
        graph[k]["pi"] = "NIL"
        graph[k]["neighbours"] = v
    time = 0
    for k in graph:
        if graph[k]["color"] == "WHITE":
            dfs_visit(graph, k, time)

def dfs_visit(graph, toVisit, time):
    time = time + 1
    graph[toVisit]["distance"] = time
    graph[toVisit]["color"] = "GRAY"
    for n in graph[toVisit]["neighbours"]:
        if graph[n]["color"] == "WHITE":
            graph[n]["pi"] = toVisit
            dfs_visit(graph, n, time)
    graph[toVisit]["color"] = "BLACK"
    time = time + 1
    graph[toVisit]["f"] = time


# Test
dfs(g)
print(g)

# ********* Connected components (directed) ********* #
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

# ********* Topological sorting ********* #

if __name__ == '__main__':
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    grid2 = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    print("The number of islands is:", numIslands(grid2))
