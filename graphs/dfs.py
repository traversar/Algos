def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()

    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(graph, neighbour, visited)
    return visited
