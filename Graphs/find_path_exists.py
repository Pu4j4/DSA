#brute force
from collections import defaultdict
def valid_path(self, n, edges, source, destination):
    graph = defaultdict(list)

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = set()

    def dfs(node):
        if node == destination:
            return True

        visited.add(node)

        for nei in graph[node]:
            if nei not in visited:
                if dfs(nei):
                    return True
        return False

    return dfs(source)


#optimized code
def valid_path(self, n, edges, source, destination):
    parent = [i for i in range(n)]

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(a, b):
        rootA = find(a)
        rootB = find(b)
        if rootA != rootB:
            parent[rootB] = rootA

    for u, v in edges:
        union(u, v)

    return find(source) == find(destination)


