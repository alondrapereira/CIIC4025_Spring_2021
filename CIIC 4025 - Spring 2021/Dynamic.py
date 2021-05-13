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

# *************** Sequence Analysis *************** #

# *************** 0-1 Knapsack *************** #

# *************** Rod Cutting *************** #

# *************** Change Making *************** #


if __name__ == '__main__':
    example_graph = {
        's': {'t': 6, 'y': 7},
        't': {'x': 5, 'z': -4, 'y': 8},
        'y': {'z': 9, 'x': -3},
        'z': {'x': 7, 's': 2},
        'x': {'t': -2}
    }
    print("Bellman-Ford result: ", get_distances(example_graph, 's'))
    print("Fibonacci result: ", fibonacci_number(9))
    print("Unique binary search trees: ", num_trees(2))
    print("Minimum Steps Required to convert w1 to w2 : ", min_distance('carat', 'casis'))

