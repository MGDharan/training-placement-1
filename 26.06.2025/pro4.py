def has_cycle(graph):
    visited = set()
    rec_stack = set()

    def dfs(v):
        visited.add(v)
        rec_stack.add(v)
        for neighbor in graph[v]:
            if neighbor not in visited and dfs(neighbor):
                return True
            elif neighbor in rec_stack:
                return True
        rec_stack.remove(v)
        return False

    return any(dfs(node) for node in graph if node not in visited)
