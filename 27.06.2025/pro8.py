def kruskal(n, edges):
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(x, y):
        xr, yr = find(x), find(y)
        if xr != yr:
            parent[yr] = xr
            return True
        return False

    mst = []
    edges.sort(key=lambda x: x[2])

    for u, v, w in edges:
        if union(u, v):
            mst.append((u, v, w))
    return mst

edges = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]
print(kruskal(4, edges))
