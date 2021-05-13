# *************** Bellman-Ford Algorithm *************** #
def get_distances(graph, source_vertex):
    distances = {}
    # First, define each vertex in the graph as an infinite number.
    for vertex in graph:
        distances[vertex] = float("inf")
    # Set the value of the first vertex equal to 0.
    distances[source_vertex] = 0
    for i in range(1, len(graph)):
        for vertex, edges in graph.items():
            for edge, weight in edges.items():
                # If the distance between the vertex and edge is lower than the current, store it.
                if distances[vertex] != float("inf") and distances[vertex] + weight < distances[edge]:
                    distances[edge] = distances[vertex] + weight
    return distances


# *************** Fibonacci Number *************** #
def fibonacci_number(n):
    A = [0, 1]
    for i in range(2, n + 1):
        A.append(A[i - 1] + A[i - 2])
    return A[n]


# *************** Binary Search Tree *************** #
# Given n, how many structurally unique binary search trees store vales 1 to n?
def num_trees(n):
    A = [0 for i in range(n + 1)]
    A[0] = 1
    for i in range(1, n + 1):
        for k in range(0, i):
            A[i] += A[k] * A[i - 1 - k]
    return A[n]


# *************** Edit Distance *************** #
def min_distance(word1, word2):
    d = [[0 for j in range(len(word2) + 1)] for i in range(len(word1) + 1)]
    for i in range(len(word1) + 1):
        d[i][0] = i
    for j in range(len(word2) + 1):
        d[0][j] = j
    for i in range(1, len(word1) + 1):
        for j in range(1, len(word2) + 1):
            if word1[i - 1] == word2[j - 1]:
                d[i][j] = d[i - 1][j - 1]
            else:
                d[i][j] = 1 + min(min(d[i - 1][j], d[i][j - 1]), d[i - 1][j - 1])
    return d[len(word1)][len(word2)]


# *************** Longest Common Subsequence *************** #
# Dynamic Programming implementation of LCS problem
def lcs(s1, s2):
    # find the length of the strings
    m = len(s1)
    n = len(s2)
    # declaring the array for storing the dp values
    L = [[None] * (n + 1) for i in range(m + 1)]
    """Following steps build L[m + 1][n + 1] in bottom up fashion
    Note: L[i][j] contains length of LCS of s1[0..i-1]
    and s2[0..j-1]"""
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif s1[i - 1] == s2[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])
    # L[m][n] contains the length of LCS of s1[0..n-1] & s2[0..m-1]
    return L[m][n]


# *************** Sequence Alignment *************** #
def sequence_alignment(s1, s2):
    # TODO
    print('this is hell :c')


# *************** 0-1 Knapsack *************** #
# A Dynamic Programming based Python
# Program for 0-1 Knapsack problem
# Returns the maximum value that can
# be put in a knapsack of capacity W
def knapsack_01(W, wt, val, n):
    A = [[0 for x in range(W + 1)] for x in range(n + 1)]
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                A[i][w] = 0
            elif wt[i - 1] <= w:
                # A[i - 1, x- wi] + vi, A[i-1, x]
                A[i][w] = max(A[i - 1][w - wt[i - 1]] + val[i - 1], A[i - 1][w])
            else:
                A[i][w] = A[i - 1][w]
    return A[n][W]

# *************** Rod Cutting *************** #

# *************** Change Making *************** #

# *************** Activity Selection *************** #


if __name__ == '__main__':
    # Input values

    # Bellman-Ford:
    example_graph = {
        's': {'t': 6, 'y': 7},
        't': {'x': 5, 'z': -4, 'y': 8},
        'y': {'z': 9, 'x': -3},
        'z': {'x': 7, 's': 2},
        'x': {'t': -2}
    }
    # Knapsack 0-1:
    val = [3, 2, 4, 4]
    wt = [4, 3, 2, 4]
    W = 6
    n = len(val)

    print("Bellman-Ford result: ", get_distances(example_graph, 's'))
    print("Fibonacci result: ", fibonacci_number(9))
    print("Unique binary search trees: ", num_trees(2))
    print("Minimum Steps Required to convert w1 to w2 : ", min_distance('carat', 'casis'))
    print("Longest Common Subsequence: ", lcs('bacad', 'accbadcb'))
    print("Sequence Analysis Result: ", sequence_alignment('AGCGCT', 'AGCCA'))
    print("Knapsack 0-1 Optimal Solution: ", knapsack_01(W, wt, val, n))
