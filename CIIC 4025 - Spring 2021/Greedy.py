from collections import defaultdict
import heapq


# *************** Prim's Algorithm *************** #
def create_spanning_tree(graph, vertex):
    mst = defaultdict(set)
    # Add given vertex to the visited_vertices
    visited_vertices = set([vertex])
    edges = []
    for next_vertex, value in graph[vertex].items():
        edges.append((value, vertex, next_vertex))
    # Convert edges into a heap
    heapq.heapify(edges)
    # This loop will continue until there are no edges left
    while edges:
        # Remove and return the smallest edge from edges
        value, initial_vertex, next_vertex = heapq.heappop(edges)
        if next_vertex not in visited_vertices:  # Only unvisited vertices must be considered to avoid cycles
            mst[initial_vertex].add(next_vertex)  # Add vertex to the minimum spanning tree
            visited_vertices.add(next_vertex)  # Add vertex to the visited vertices
            for next, value in graph[next_vertex].items():
                if next not in visited_vertices:
                    heapq.heappush(edges, (value, next_vertex, next))  # Add remaining vertices to edges
    return mst


# *************** Dijkstra's Algorithm *************** #

# *************** Activity Selection *************** #

# *************** Fractional Knapsack *************** #
# Python3 program to solve fractional
# Knapsack Problem


class ItemValue:
    """Item Value DataClass"""

    def __init__(self, wt, val, ind):
        self.wt = wt
        self.val = val
        self.ind = ind
        self.cost = val // wt

    def __lt__(self, other):
        return self.cost < other.cost


# Greedy Approach

class FractionalKnapSack:
    """Time Complexity O(n log n)"""

    @staticmethod
    def getMaxValue(wt, val, capacity):
        """function to get maximum value """
        iVal = []
        for i in range(len(wt)):
            iVal.append(ItemValue(wt[i], val[i], i))

        # sorting items by value
        iVal.sort(reverse=True)

        totalValue = 0
        for i in iVal:
            curWt = int(i.wt)
            curVal = int(i.val)
            if capacity - curWt >= 0:
                capacity -= curWt
                totalValue += curVal
            else:
                fraction = capacity / curWt
                totalValue += curVal * fraction
                capacity = int(capacity - (curWt * fraction))
                break
        return totalValue


# Driver Code
if __name__ == "__main__":
    # wt = [10, 40, 20, 30]
    # val = [60, 40, 100, 120]
    # capacity = 50
    wt = [5, 20, 10, 12]
    val = [50, 140, 60, 60]
    capacity = 30
    print("Maximum value in Fractional Knapsack =", FractionalKnapSack.getMaxValue(wt, val, capacity))


# This code is contributed by vibhu4agarwal

# *************** Change Making *************** #

# *************** Huffman Coding *************** #
