"""


8 Puzzle problem in Python
The 8 puzzle problem solution is covered in this article. A 3 by 3 board with 8 tiles (each tile has a number from 1 to 8) and a single empty space is provided. The goal is to use the vacant space to arrange the numbers on the tiles such that they match the final arrangement. Four neighbouring (left, right, above, and below) tiles can be moved into the available area.

For instance,

8 Puzzle problem in Python
1. DFS (Brute - Force) :
On the state-space tree (Set of all configurations of a particular issue, i.e., all states that may be reached from the beginning state), we can do a depth-first search.

8 Puzzle problem in Python
Figure : 8 Puzzle's State Space Tree
Play Video

In this solution, further movements might not always send us closer to the objective, but rather further away. Regardless of the initial state, the state-space tree searches down the leftmost route from the root. With this method, an answer node might never be discovered.

2. BFS (Brute - Force) :
We can search the state space tree using a breadth-first approach. It always locates the goal state that is closest to the root. However, the algorithm tries the same series of movements as DFS regardless of the initial state.

3. Branch and Bound :
By avoiding searching in sub-trees which do not include an answer node, an "intelligent" ranking function, also known as an approximatsion costs function, may frequently speed up the search for an answer node. However, instead of using the backtracking method, it does a BFS-style search.

Basically, Branch and Bound involves three different kinds of nodes.

A live node is a created node whose children have not yet been formed.
The offspring of the E-node which is a live node, are now being investigated. Or to put it another way, an E-node is a node that is currently expanding.
A created node which is not to be developed or examined further is referred to as a dead node. A dead node has already extended all of its offspring.
Costs function :
In the search tree, each node Y has a corresponding costs. The next E-node may be found using the costs function. The E-node with the lowest costs is the next one. The function can be defined as :

C(Y) = g(Y) + h(Y)
where
   g(Y) = the costs of reaching to the current node
          from the root.
   h(Y) = the costs of reaching to an answer node from the Y.
The optimum costs function for an algorithm for 8 puzzles is :

We suppose that it will costs one unit to move a tile in any direction. In light of this, we create the following costs function for the 8-puzzle algorithm :

c(y) = f(y) + h(y)
where
   f(y) = the path's total length from the root y.
   and
   h(y) = the amount of the non-blank tiles which are not in
        their final goal position (misplaced tiles).

To change state y into a desired state, there are at least h(y) movements required.
There is an algorithm for estimatsing the unknown value of h(y), which is accessible.


Final algorithm :
In order to maintain the list of live nodes, algorithm LCSearch employs the functions Least() and Add().
Least() identifies a live node with the least c(y), removes it from the list, and returns it.
Add(y) adds y to the list of live nodes.
Add(y) implements the list of live nodes as a min-heap.
The route taken by the aforementioned algorithm to arrive at the final configuration of the 8-Puzzle from the starting configuration supplied is shown in the diagram below. Keep in mind that only nodes with the lowest costs function value are extended.

8 Puzzle problem in Python
"""

# Python code to display the way from the root
# node to the final destination node for N*N-1 puzzle
# algorithm by the help of Branch and Bound technique
# The answer assumes that the instance of the
# puzzle can be solved

# Importing the 'copy' for deepcopy method
import copy

# Importing the heap methods from the python
# library for the Priority Queue
from heapq import heappush, heappop

# This particular var can be changed to transform
# the program from 8 puzzle(n=3) into 15
# puzzle(n=4) and so on ...
n = 3

# bottom, left, top, right
rows = [1, 0, -1, 0]
cols = [0, -1, 0, 1]


# creating a class for the Priority Queue
class priorityQueue:

    # Constructor for initializing a
    # Priority Queue
    def __init__(self):
        self.heap = []

        # Inserting a new key 'key'

    def push(self, key):
        heappush(self.heap, key)

        # funct to remove the element that is minimum,

    # from the Priority Queue
    def pop(self):
        return heappop(self.heap)

        # funct to check if the Queue is empty or not

    def empty(self):
        if not self.heap:
            return True
        else:
            return False

        # structure of the node


class nodes:

    def __init__(self, parent, mats, empty_tile_posi,
                 costs, levels):
        # This will store the parent node to the
        # current node And helps in tracing the
        # path when the solution is visible
        self.parent = parent

        # Useful for Storing the matrix
        self.mats = mats

        # useful for Storing the position where the
        # empty space tile is already existing in the matrix
        self.empty_tile_posi = empty_tile_posi

        # Store no. of misplaced tiles
        self.costs = costs

        # Store no. of moves so far
        self.levels = levels

        # This func is used in order to form the

    # priority queue based on
    # the costs var of objects
    def __lt__(self, nxt):
        return self.costs < nxt.costs

    # method to calc. the no. of


# misplaced tiles, that is the no. of non-blank
# tiles not in their final posi
def calculateCosts(mats, final) -> int:
    count = 0
    for i in range(n):
        for j in range(n):
            if ((mats[i][j]) and
                    (mats[i][j] != final[i][j])):
                count += 1

    return count


def newNodes(mats, empty_tile_posi, new_empty_tile_posi,
             levels, parent, final) -> nodes:
    # Copying data from the parent matrixes to the present matrixes
    new_mats = copy.deepcopy(mats)

    # Moving the tile by 1 position
    x1 = empty_tile_posi[0]
    y1 = empty_tile_posi[1]
    x2 = new_empty_tile_posi[0]
    y2 = new_empty_tile_posi[1]
    new_mats[x1][y1], new_mats[x2][y2] = new_mats[x2][y2], new_mats[x1][y1]

    # Setting the no. of misplaced tiles
    costs = calculateCosts(new_mats, final)

    new_nodes = nodes(parent, new_mats, new_empty_tile_posi,
                      costs, levels)
    return new_nodes


# func to print the N by N matrix
def printMatsrix(mats):
    for i in range(n):
        for j in range(n):
            print("%d " % (mats[i][j]), end=" ")

        print()

    # func to know if (x, y) is a valid or invalid


# matrix coordinates
def isSafe(x, y):
    return x >= 0 and x < n and y >= 0 and y < n


# Printing the path from the root node to the final node
def printPath(root):
    if root == None:
        return

    printPath(root.parent)
    printMatsrix(root.mats)
    print()


# method for solving N*N - 1 puzzle algo
# by utilizing the Branch and Bound technique. empty_tile_posi is
# the blank tile position initially.
def solve(initial, empty_tile_posi, final):
    # Creating a priority queue for storing the live
    # nodes of the search tree
    pq = priorityQueue()

    # Creating the root node
    costs = calculateCosts(initial, final)
    root = nodes(None, initial,
                 empty_tile_posi, costs, 0)

    # Adding root to the list of live nodes
    pq.push(root)

    # Discovering a live node with min. costs,
    # and adding its children to the list of live
    # nodes and finally deleting it from
    # the list.
    while not pq.empty():

        # Finding a live node with min. estimatsed
        # costs and deleting it form the list of the
        # live nodes
        minimum = pq.pop()

        # If the min. is ans node
        if minimum.costs == 0:
            # Printing the path from the root to
            # destination;
            printPath(minimum)
            return

            # Generating all feasible children
        for i in range(n):
            new_tile_posi = [
                minimum.empty_tile_posi[0] + rows[i],
                minimum.empty_tile_posi[1] + cols[i], ]

            if isSafe(new_tile_posi[0], new_tile_posi[1]):
                # Creating a child node
                child = newNodes(minimum.mats,
                                 minimum.empty_tile_posi,
                                 new_tile_posi,
                                 minimum.levels + 1,
                                 minimum, final, )

                # Adding the child to the list of live nodes
                pq.push(child)

            # Main Code


# Initial configuration
# Value 0 is taken here as an empty space
initial = [[1, 2, 3],
           [5, 6, 0],
           [7, 8, 4]]

# Final configuration that can be solved
# Value 0 is taken as an empty space
final = [[1, 2, 3],
         [5, 8, 6],
         [0, 7, 4]]

# Blank tile coordinates in the
# initial configuration
empty_tile_posi = [1, 2]

# Method call for solving the puzzle
solve(initial, empty_tile_posi, final)