# Breadth first search
from collections import deque


def nearest_restaurant(graph, start, restaurants):
    q = deque([start])
    visited = set([start])

    while q:
        node = q.popleft()
        if node in restaurants:
            return node  # nearest restaurant

        for nei in graph[node]:
            if nei not in visited:
                visited.add(nei)
                q.append(nei)

    return None


graphs = {"A": ["B", "C"], "B": ["A", "D"], "C": ["A", "E"], "D": ["B"], "E": ["C"]}

print("-" * 40)
print("Breadth First Search: ")
print("-" * 40)
print(nearest_restaurant(graphs, "A", {"E", "D"}))
print("-" * 40)
print("\n")


def has_cycle(graph):
    visited = set()

    def dfs(node, parent):
        visited.add(node)
        for nei in graph[node]:
            if nei not in visited:
                if dfs(nei, node):
                    return True
            elif nei != parent:
                return True
        return False

    for node in graph:
        if node not in visited:
            if dfs(node, None):
                return True
    return False
