"""
DFS Basics
For traversing a graph we can take two approaches. We can go level-by-level or
 we can go to the depth as far as possible.

DFS takes the second approach. It starts with a root node and explores the graph in-depth
 as far as possible. After reaching a dead-end, the algorithm
  starts backtracking and eventually completes the search.


"""


def dfs(graph, source, visited, dfs_traversal):
    if source not in visited:
        dfs_traversal.append(source)
        visited.add(source)

        for neighbor_node in graph[source]:
            dfs(graph, neighbor_node, visited, dfs_traversal)

    return dfs_traversal


def main():
    A = input("Enter Root \n")
    B = input("Enter Node \n")
    C = input("Enter Node \n")
    D = input("Enter Node \n")
    E = input("Enter Node\n")
    F = input("Enter Node \n")
    G = input("Enter Node \n")
    visited = set()
    dfs_traversal = list()

    graph = {
        A: [B, C],
        B: [D, E],
        C: [F, G],
        D: [],
        E: [],
        F: [],
        G: []
    }

    print(f"DFS: {dfs(graph, A, visited, dfs_traversal)}")


if __name__=="__main__":
    main()