from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}


def bfs(graph, start, goal):
    visited = []
    queue = deque([[start]])

    while queue:
        path = queue.popleft()
        node = path[-1]
        if node == goal:
            return path
        if node not in visited:
            visited.append(node)
            for neighbor in graph[node]:
                queue.append(path + [neighbor])
    return None


def dfs(graph, start, goal):
    visited = []
    stack = [[start]]

    while stack:
        path = stack.pop()
        node = path[-1]
        if node == goal:
            return path
        if node not in visited:
            visited.append(node)
            for neighbor in reversed(graph[node]):
                stack.append(path + [neighbor])
    return None


print("BFS path A to F:", bfs(graph, 'A', 'F'))
print("DFS path A to F:", dfs(graph, 'A', 'F'))
print("BFS path A to Z:", bfs(graph, 'A', 'Z'))