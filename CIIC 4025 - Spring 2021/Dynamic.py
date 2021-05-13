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

# *************** Binary Search Tree *************** #

# *************** Edit Distance *************** #

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
    print(get_distances(example_graph, 's'))
