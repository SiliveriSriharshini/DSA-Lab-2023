from collections import defaultdict
from queue import Queue
from heapq import heappush, heappop

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def add_edge(self, u, v, w):
        self.graph[u].append((v, w))
        self.graph[v].append((u, w))

    def bfs(self, start):
        visited = [False] * self.V
        queue = Queue()
        queue.put(start)
        visited[start] = True

        while queue:
            curr = queue.get(0)
            print(curr, end=' ')

            for neighbor in self.graph[curr]:
                if not visited[neighbor[0]]:
                    visited[neighbor[0]] = True
                    queue.put(neighbor[0])

    def dfs(self, start):
        visited = [False] * self.V
        self._dfs_helper(start, visited)

    def _dfs_helper(self, curr, visited):
        visited[curr] = True
        print(curr, end=' ')

        for neighbor in self.graph[curr]:
            if not visited[neighbor[0]]:
                self._dfs_helper(neighbor[0], visited)

    def prim(self):
        visited = [False] * self.V
        heap = [(0, 0)]
        mst = []

        while heap:
            weight, curr = heappop(heap)

            if visited[curr]:
                continue

            visited[curr] = True
            mst.append((curr, weight))

            for neighbor, w in self.graph[curr]:
                if not visited[neighbor]:
                    heappush(heap, (w, neighbor))

        return mst

    def kruskal(self):
        edges = []
        for u in self.graph:
            for v, w in self.graph[u]:
                edges.append((w, u, v))

        edges.sort()
        parent = list(range(self.V))
        mst = []

        def find(u):
            if parent[u] != u:
                parent[u] = find(parent[u])
            return parent[u]

        def union(u, v):
            parent[find(u)] = find(v)

        for w, u, v in edges:
            if find(u) != find(v):
                union(u, v)
                mst.append((u, v, w))

        return mst

if __name__ == '__main__':
    graph = Graph(5)

    graph.add_edge(0, 1, 2)
    graph.add_edge(0, 3, 6)
    graph.add_edge(1, 2, 3)
    graph.add_edge(1, 3, 8)
    graph.add_edge(1, 4, 5)
    graph.add_edge(2, 4, 7)
    graph.add_edge(3, 4, 9)

    print("BFS Traversal:")
    graph.bfs(0)
    print()

    print("DFS Traversal:")
    graph.dfs(0)
    print()

    '''print("Minimum Spanning Tree using Prim's Algorithm:")
    mst = graph.prim()
    for u, w in mst:
        print(f"(0, {u}) = {w}")

    print("Minimum Spanning Tree using Kruskal's Algorithm:")
    mst = graph.kruskal()
    for u, v, w in mst:
        print(f"({u}, {v}) = {w}")'''