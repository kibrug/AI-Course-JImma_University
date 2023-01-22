"""
Iterative Deepening Depth-First Search Algorithm
The Iterative Deepening Depth-First Search (also ID-DFS) algorithm is an algorithm used to find a node in a tree. This means that given a tree data structure, the algorithm will return the first node in this tree that matches the specified condition. Nodes are sometimes referred to as vertices (plural of vertex) - here, we’ll call them nodes. The edges have to be unweighted. This algorithm can also work with unweighted graphs if mechanism to keep track of already visited nodes is added.

Description of the Algorithm
The basic principle of the algorithm is to start with a start node, and then look at the first child of this node. It then looks at the first child of that node (grandchild of the start node) and so on, until a node has no more children (we’ve reached a leaf node). It then goes up one level, and looks at the next child. If there are no more children, it goes up one more level, and so on, until it find more children or reaches the start node. If hasn’t found the goal node after returning from the last child of the start node, the goal node cannot be found, since by then all nodes have been traversed.

So far this has been describing Depth-First Search (DFS). Iterative deepening adds to this, that the algorithm not only returns one layer up the tree when the node has no more children to visit, but also when a previously specified maximum depth has been reached. Also, if we return to the start node, we increase the maximum depth and start the search all over, until we’ve visited all leaf nodes (bottom nodes) and increasing the maximum depth won’t lead to us visiting more nodes.

There are two common ways to traverse a graph, BFS and DFS. Considering a Tree (or Graph) of huge height and width, both BFS and DFS are not very efficient due to following reasons.

DFS first traverses nodes going through one adjacent of root, then next adjacent. The problem with this approach is, if there is a node close to root, but not in first few subtrees explored by DFS, then DFS reaches that node very late. Also, DFS may not find shortest path to a node (in terms of number of edges).
BFS goes level by level, but requires more space. The space required by DFS is O(d) where d is depth of tree, but space required by BFS is O(n) where n is number of nodes in tree (Why? Note that the last level of tree can have around n/2 nodes and second last level n/4 nodes and in BFS we need to have every level one by one in queue).
IDDFS combines depth-first search’s space-efficiency and breadth-first search’s fast search (for nodes closer to root).

How does IDDFS work?
IDDFS calls DFS for different depths starting from an initial value. In every call, DFS is restricted from going beyond given depth. So basically we do DFS in a BFS fashion.


Algorthem

// Returns true if target is reachable from
// src within max_depth
bool IDDFS(src, target, max_depth)
    for limit from 0 to max_depth
       if DLS(src, target, limit) == true
           return true
    return false

bool DLS(src, target, limit)
    if (src == target)
        return true;

    // If reached the maximum depth,
    // stop recursing.
    if (limit <= 0)
        return false;

    foreach adjacent i of src
        if DLS(i, target, limit?1)
            return true

    return false
An important thing to note is, we visit top level nodes multiple times. The last (or max depth) level is visited once, second last level is visited twice, and so on. It may seem expensive, but it turns out to be not so costly, since in a tree most of the nodes are in the bottom level. So it does not matter much if the upper levels are visited multiple times. Below is implementation of above algorithm
"""

# Python program to print DFS traversal from a given
# given graph
from collections import defaultdict

# This class represents a directed graph using adjacency
# list representation
class Graph:

	def __init__(self,vertices):

		# No. of vertices
		self.V = vertices

		# default dictionary to store graph
		self.graph = defaultdict(list)

	# function to add an edge to graph
	def addEdge(self,u,v):
		self.graph[u].append(v)

	# A function to perform a Depth-Limited search
	# from given source 'src'
	def DLS(self,src,target,maxDepth):

		if src == target : return True

		# If reached the maximum depth, stop recursing.
		if maxDepth <= 0 : return False

		# Recur for all the vertices adjacent to this vertex
		for i in self.graph[src]:
				if(self.DLS(i,target,maxDepth-1)):
					return True
		return False

	# IDDFS to search if target is reachable from v.
	# It uses recursive DLS()
	def IDDFS(self,src, target, maxDepth):

		# Repeatedly depth-limit search till the
		# maximum depth
		for i in range(maxDepth):
			if (self.DLS(src, target, i)):
				return True
		return False

# Create a graph given in the above diagram
g = Graph (7);
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 3)
g.addEdge(1, 4)
g.addEdge(2, 5)
g.addEdge(2, 6)

target = 6; maxDepth = 3; src = 0

if g.IDDFS(src, target, maxDepth) == True:
	print ("Target is reachable from source " +
		"within max depth")
else :
	print ("Target is NOT reachable from source " +
		"within max depth")

# This code is contributed by Neelam Pandey
