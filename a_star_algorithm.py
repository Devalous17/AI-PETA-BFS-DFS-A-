import heapq

graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'D': 2, 'E': 5},
    'C': {'F': 3},
    'D': {'F': 4},
    'E': {'F': 1},
    'F': {}
}

heuristic = {
    'A': 6,
    'B': 4,
    'C': 3,
    'D': 3,
    'E': 1,
    'F': 0
}


def a_star(graph, start, goal, heuristic):
    queue = [(heuristic[start], 0, start, [start])]
    visited = set()

    while queue:
        f_cost, g_cost, node, path = heapq.heappop(queue)

        if node == goal:
            return path

        if node not in visited:
            visited.add(node)

            for neighbor, cost in graph[node].items():
                new_g = g_cost + cost
                new_f = new_g + heuristic[neighbor]

                heapq.heappush(
                    queue,
                    (new_f, new_g, neighbor, path + [neighbor])
                )

    return None


print("A* path A to F:", a_star(graph, 'A', 'F', heuristic))
