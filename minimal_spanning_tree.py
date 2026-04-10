def kruskal(n, edges):
    parent = list(range(n))

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(a, b):
        pa, pb = find(a), find(b)
        if pa == pb:
            return False
        parent[pb] = pa
        return True

    edges.sort(key=lambda x: x[2])  # sort by weight
    mst = []
    cost = 0

    for u, v, w in edges:
        if union(u, v):
            mst.append((u, v, w))
            cost += w

    return mst, cost


edges = [(0, 1, 4), (0, 2, 3), (1, 2, 1), (1, 3, 2), (2, 3, 4)]

print(kruskal(4, edges))
