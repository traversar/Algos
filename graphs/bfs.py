def bfs(graph, node):
    visited = []
    queue = []
    visited.append(node)
    queue.append(node)

    while queue:
        curr = queue.pop(0)
        print (curr, end = " ")

        for neighbour in graph[curr]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
