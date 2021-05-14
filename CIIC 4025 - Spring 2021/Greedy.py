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

"""Sorted"""

"""Prints a maximum set of activities that can be done by a
single person, one at a time"""


# n --> Total number of activities
# s[]--> An array that contains start time of all activities
# f[] --> An array that contains finish time of all activities

def printMaxActivities(s, f):
    n = len(f)
    print("The following activities are selected")

    # The first activity is always selected
    i = 0
    print(i),

    # Consider rest of the activities
    for j in range(n):

        # If this activity has start time greater than
        # or equal to the finish time of previously
        # selected activity, then select it
        if s[j] >= f[i]:
            print(j),
            i = j


# Driver program to test above function
s = [1, 3, 0, 5, 8, 5]
f = [2, 4, 6, 7, 9, 9]
printMaxActivities(s, f)

# This code is contributed by Nikhil Kumar Singh

''' Not sorted.'''


def MaxActivities(arr, n):
    selected = []

    # Sort jobs according to finish time
    Activity.sort(key=lambda x: x[1])

    # The first activity always gets selected
    i = 0
    selected.append(arr[i])

    for j in range(1, n):

        '''If this activity has start time greater than or
           equal to the finish time of previously selected
           activity, then select it'''
        if arr[j][0] >= arr[i][1]:
            selected.append(arr[j])
            i = j
    return selected


# Driver code
Activity = [[5, 9], [1, 2], [3, 4], [0, 6], [5, 7], [8, 9]]
n = len(Activity)
selected = MaxActivities(Activity, n)
print("Following activities are selected :")
print(selected)


# *************** Fractional Knapsack *************** #
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
    wt = [5, 20, 10, 12]
    val = [50, 140, 60, 60]
    capacity = 30
    print("Maximum value in Fractional Knapsack =", getMaxValue(wt, val, capacity))

# *************** Change Making *************** #

# *************** Huffman Coding *************** #
