

"""Breadth-First Search (BFS) Algorithm With Python

1. Start with a root node and push it to the queue.
2. Mark the root node as visited and print it
3. Continue a loop until the queue is empty:
   3.1. Pop the front node from the queue
   3.2. Push the child/neighbor nodes of the front node to the queue
   3.3  Mark them as visited and print
   
"""

def bfs(graph, source):
    visited = set()  # to keep track of already visited nodes
    bfs_traversal = list()  # the BFS traversal result
    queue = list()  # queue

    # push the root node to the queue and mark it as visited
    queue.append(source)
    visited.add(source)

    # loop until the queue is empty
    while queue:
        # pop the front node of the queue and add it to bfs_traversal
        current_node = queue.pop(0)
        bfs_traversal.append(current_node)

        # check all the neighbour nodes of the current node
        for neighbour_node in graph[current_node]:
            # if the neighbour nodes are not already visited,
            # push them to the queue and mark them as visited
            if neighbour_node not in visited:
                visited.add(neighbour_node)
                queue.append(neighbour_node)

    return bfs_traversal


def main():
    A = input("Enter Root\n")
    B = input("Enter Next  To Root Node\n")
    C = input("Enter Next Node\n")
    D = input("Enter Next Node\n")
    E = input("Enter Next  Node\n")
    F= input("Enter Last Node\n")


    graph = {
        A: [B, C, D],
        B: [A, D, E],
        C: [A, D],
        D: [B, C, A, E],
        E: [E, D]
    }

    bfs_traversal = bfs(graph, A)
    print(f"BFS: {bfs_traversal}")


if __name__ == '__main__':
    main()